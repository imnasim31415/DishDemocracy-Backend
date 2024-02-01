from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import RestaurantForm, EmployeeForm, MenuForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from .models import *
                    # login(request,authenticate(request,username=loginOwner.username,email=loginOwner.email,password=loginOwner.password))

# Create your views here.
def home(request):
    if 'employee' in request.POST:
            checker=Employee.objects.filter(email=request.POST.get('email'))
            if not checker:
                messages.error(request,'Account does not exist',extra_tags='painai')
            else:
                print(request.POST.get('email'))
                employee=Employee.objects.get(email=request.POST.get('email'))
                password=request.POST.get('password')
                if employee.password!=password:
                    messages.error(request,'Passwords do not match!',extra_tags='painai')
                else:
                   login(request,authenticate(request,username=employee.username,email=employee.email,password=employee.password))
                   return(redirect('/employee_page'))
    if 'owner' in request.POST:
            checker=Restaurant.objects.filter(rest_email=request.POST.get('email'))
            if not checker:
                messages.error(request,'Account does not exist',extra_tags='painai')
            else:
                print(request.POST.get('email'))
                owner=Restaurant.objects.get(rest_email=request.POST.get('email'))
                password=request.POST.get('password')
                if owner.rest_password!=password:
                    messages.error(request,'Passwords do not match!',extra_tags='painai')
                else:
                   login(request,authenticate(request,username=owner.username,email=owner.rest_email,password=owner.rest_password))
                   return(redirect('/restaurant_page'))
            
    return render(request, 'home.html')



def newPage(request):
    return render(r)

def employee_page(request):
    return render(request, 'employee_page.html')


def restaurant_page(request):
    return render(request, 'restaurant_page.html')
def register(request):
    if 'owner' in request.POST:
                 ownerEmail=request.POST.get('email')
                 ownerPassword=request.POST.get('password')
                 ownerUsername=request.POST.get('username')
                 restName=request.POST.get('restName')
                 createRestaurant=Restaurant(
                     rest_email=ownerEmail,
                     rest_password=ownerPassword,
                     username=ownerUsername,
                     name=restName
                 )
                 createRestaurant.save()
                 user=User.objects.create_user(username=request.POST.get('username'),email=request.POST.get('email'),password=request.POST.get('password'))
                 return redirect('/')
    return render(request,'register_restaurant.html')
def registerEmployee(request):
    if 'employee' in request.POST:
                 name=request.POST.get('name')
                 employeeEmail=request.POST.get('email')
                 employeePassword=request.POST.get('password')
                 employeeUsername=request.POST.get('username')
                 createEmployee=Employee(
                     name=name,
                     email=employeeEmail,
                     password=employeePassword,
                     username=employeeUsername,
                 )
                 createEmployee.save()
                 user=User.objects.create_user(username=request.POST.get('username'),email=request.POST.get('email'),password=request.POST.get('password'))
                 return redirect('/')
    return render(request,'register_employee.html')