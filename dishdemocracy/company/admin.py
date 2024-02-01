from django.contrib import admin
from .models import Employee, Restaurant, Menu, Vote, Result

# Register your models here.
admin.site.register(Employee)
admin.site.register(Result)
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Vote)