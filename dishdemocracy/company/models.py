from django.db import models
from datetime import date

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=50)
    prev_vote_date = models.DateField(default=date(1980, 1, 1), null=True, blank=True)
        
    def __str__(self):
        return self.name
    
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    rest_email = models.EmailField(max_length=254, unique=True)
    rest_password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    items = models.CharField(max_length=255)
    
    def __str__(self):
        return self.items




class Vote(models.Model):
    voter = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Result(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    winner = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.winner
