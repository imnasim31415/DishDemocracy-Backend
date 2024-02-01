from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import RestaurantForm, EmployeeForm, MenuForm

# Create your views here.
def home(request):
    
    return render(request, 'home.html')

def register_employee(request):
    empty_form = EmployeeForm()
    
    if request.method=='POST':
        empty_form = EmployeeForm(request.POST)
        empty_form.save()
        
        return redirect(home)
    
    return render(request, 'register_employee.html', {'form': empty_form})


def register_restaurant(request):
    empty_form = RestaurantForm()
    
    if request.method=='POST':
        empty_form = RestaurantForm(request.POST)
        empty_form.save()
        
        return redirect(home)
    
    return render(request, 'register_restaurant.html', {'form': empty_form})

def employee_page(request):
    return render(request, 'employee_page.html')


def restaurant_page(request):
    return render(request, 'restaurant_page.html')