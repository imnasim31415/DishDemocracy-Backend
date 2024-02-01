from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('register', views.register, name='register_owner'),
    path('registerEmployee/', views.registerEmployee, name='register_employee'),
    path('employee_page', views.employee_page, name='employee_page'),
    path('newpage/',views.newPage,name='newPage'),
    path('restaurant_page', views.restaurant_page, name='restaurant_page'),
]