from django.db import models
from datetime import date

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    prev_vote_date = models.DateField(default=date(1980, 1, 1), null=True, blank=True)
        
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    restaurantId=models.IntegerField(blank=True,null=True)
    name = models.CharField(max_length=255,blank=True,null=True)
    username = models.CharField(max_length=255,null=True,blank=True)
    rest_email = models.EmailField(max_length=254,null=True,blank=True)
    rest_password = models.CharField(max_length=50,null=True,blank=True)
    
    def __str__(self):
        return self.name

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    items = models.CharField(max_length=255,null=True,blank=True)
    desc=models.CharField(max_length=255,null=True,blank=True)
    image=models.ImageField(upload_to='image/',blank=True,null=True)

    def __str__(self):
        return self.items




class Vote(models.Model):
    voter = models.ForeignKey(Employee, on_delete=models.CASCADE,null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,null=True)
    date=models.DateField(null=True,blank=True)
    def __str__(self):
        return str(self.voter.name)+" "+str(self.restaurant.name)
    

class Result(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,null=True)
    date = models.DateField(null=True,blank=True)
    
    def __str__(self):
        return self.restaurant
