from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
import datetime
from .models import *

def home(request):
    if 'employee' in request.POST:
        checker = Employee.objects.filter(email=request.POST.get('email'))
        if not checker:
            messages.error(request, 'Account does not exist', extra_tags='painai')
        else:
            print(request.POST.get('email'))
            employee = Employee.objects.get(email=request.POST.get('email'))
            password = request.POST.get('password')
            if employee.password != password:
                messages.error(request, 'Passwords do not match!', extra_tags='painai')
            else:
                login(request, authenticate(request, username=employee.username, email=employee.email, password=employee.password))
                return redirect('/employee_page')
    if 'owner' in request.POST:
        checker = Restaurant.objects.filter(rest_email=request.POST.get('email'))
        if not checker:
            messages.error(request, 'Account does not exist', extra_tags='painai')
        else:
            print(request.POST.get('email'))
            owner = Restaurant.objects.get(rest_email=request.POST.get('email'))
            password = request.POST.get('password')
            if owner.rest_password != password:
                messages.error(request, 'Passwords do not match!', extra_tags='painai')
            else:
                login(request, authenticate(request, username=owner.username, email=owner.rest_email, password=owner.rest_password))
                return redirect('/restaurant_page')

    return render(request, 'home.html')

def employee_page(request):
    employee = Employee.objects.get(email=request.user.email)
    restaurantList = Restaurant.objects.filter()
    today = datetime.datetime.today()
    checker = 0
    votedList = Vote.objects.filter(voter=employee, date=today)
    if votedList:
        checker = 1
    queryDict = {}
    for o in restaurantList:
        menuList = Menu.objects.filter(restaurant=o)
        queryDict[o] = menuList
    if 'vote' in request.POST:
        restaurant = Restaurant.objects.get(restaurantId=int(request.POST.get('vote')))
        vote = Vote(
            restaurant=restaurant,
            voter=employee,
            date=today
        )
        vote.save()
        return redirect('/employee_page')

    cont = {
        'queryDict': queryDict,
        'checker': checker
    }
    return render(request, 'employee_page.html', cont)

def winner(request):
    today = datetime.datetime.today()
    queryDict = {}
    restaurantList = Vote.objects.filter(date=today)
    for o in restaurantList:
        queryDict[o.restaurant.restaurantId] = 0
    for o in restaurantList:
        queryDict[o.restaurant.restaurantId] += 1
    sortedList = sorted(queryDict.items(), key=lambda x: x[1], reverse=True)
    winnerRestaurant = sortedList[0][0]
    temp = restaurantList[0].restaurant.restaurantId

    finalDict = {}
    for o in sortedList:
        rest = Restaurant.objects.get(restaurantId=o[0])
        finalDict[rest] = o[1]
    print(winnerRestaurant)
    cont = {
        'today': today,
        'finalDict': finalDict,
        'winner': winnerRestaurant
    }
    return render(request, 'winner.html', cont)

def restaurant_page(request):
    user = request.user
    restaurant = Restaurant.objects.get(rest_email=user.email)
    menuList = Menu.objects.filter(restaurant=restaurant)
    if 'add' in request.POST:
        addMenu = Menu(
            restaurant=restaurant,
            items=request.POST.get('name'),
            image=request.FILES.get('image'),
            desc=request.POST.get('desc')
        )
        addMenu.save()
        return redirect('/restaurant_page')
    cont = {
        'menuList': menuList
    }
    return render(request, 'restaurant_page.html', cont)

def register(request):
    if 'owner' in request.POST:
        ownerEmail = request.POST.get('email')
        ownerPassword = request.POST.get('password')
        ownerUsername = request.POST.get('username')
        restName = request.POST.get('restName')
        size = len(Restaurant.objects.filter()) + 1
        createRestaurant = Restaurant(
            restaurantId=size,
            rest_email=ownerEmail,
            rest_password=ownerPassword,
            username=ownerUsername,
            name=restName
        )
        createRestaurant.save()
        user = User.objects.create_user(username=request.POST.get('username'), email=request.POST.get('email'), password=request.POST.get('password'))
        return redirect('/')
    return render(request, 'register_restaurant.html')

def registerEmployee(request):
    if 'employee' in request.POST:
        name = request.POST.get('name')
        employeeEmail = request.POST.get('email')
        employeePassword = request.POST.get('password')
        employeeUsername = request.POST.get('username')
        createEmployee = Employee(
            name=name,
            email=employeeEmail,
            password=employeePassword,
            username=employeeUsername,
        )
        createEmployee.save()
        user = User.objects.create_user(username=request.POST.get('username'), email=request.POST.get('email'), password=request.POST.get('password'))
        return redirect('/')
    return render(request, 'register_employee.html')
