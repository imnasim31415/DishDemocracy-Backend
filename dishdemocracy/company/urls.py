from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('register_employee', views.register_employee, name='register_employee'),
    path('register_restaurant', views.register_restaurant, name='register_restaurant'),
    path('employee_page', views.employee_page, name='employee_page'),
    path('restaurant_page', views.restaurant_page, name='restaurant_page'),
]