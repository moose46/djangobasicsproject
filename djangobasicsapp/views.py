import datetime
import http
from mailbox import Message
from math import log
from re import template
from urllib import request

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# function based view
# http://127.0.0.1:8000/djangobasicsapp/Home
def Home(request):
    return HttpResponse("<h1>Hello World! Django 5.0.4</h1>")


def Index(request):
    return render(request, "djangobasicsapp/Index.html")


def ShowMoreMessage(request):
    return HttpResponse(
        "<h1>Hello World! Django 5.0.4</h1><h2>Hello World! Django 5.0.4</h2><h3>Hello World! Django 5.0.4</h3>"
    )


# http://127.0.0.1:8000/djangobasicsapp/UseVariables
def UseVariablesAsResponse(request):
    Message = "<h1>Welcome to Django Development.</h1>"
    Message += "<h2>Welcome to Django Development.</h2>"
    Message += "<h3>Welcome to Django Development.</h3>"
    Message += "<h4>Welcome to Django Development.</h4>"
    Message += "<h5>Welcome to Django Development.</h5>"
    return HttpResponse(Message)


# http://127.0.0.1:8000/djangobasicsapp/GetRequestDemo?Country=Bite%20Me
def GetRequestVariables(request):
    # GET,POST, PUT,DELETE,PATCH
    Message = ""
    if request.method == "GET":
        if request.GET.get("Message"):
            Message = request.GET.get("Message")
        else:
            Message = "<h1>You haven't supplied value for Message Parameter ...</h1>"
    if request.method == "GET":
        if request.GET.get("Country"):
            Message += request.GET.get("Country")
        else:
            Message += "<h1>You haven't supplied value for Country Parameter ...</h1>"
    return HttpResponse(Message)


from datetime import date, datetime


# http://127.0.0.1:8000/djangobasicsapp/ShowTime
def ShowDateTimeInfo(request):
    TodaysDate = datetime.now()
    templatefilename = "djangobasicsapp/ShowTimeInfo.html"
    context = {"TodaysDate": TodaysDate}
    return render(request, templatefilename, context)


import logging


# http://127.0.0.1:8000/djangobasicsapp/LoggingDemo
def LogginExample(request):
    logging.debug(f"Debug : I just entered into the View .. {datetime.now()}")
    logging.info(f"Info : Confirmation that things are working as excpected ")
    logging.warning(f"Warning : An indication that something unexpected happened ")
    logging.error(f"Error : Due to a more serious problem ")
    logging.critical(
        f"Critical : A serious error, indicating that the program itself may not be able to contine"
    )

    custom_logger = logging.getLogger("mycustom_logger")
    custom_logger.debug(f"Debug : I just entered into the View .. {datetime.now()}")
    custom_logger.info(f"Info : Confirmation that things are working as excpected ")
    custom_logger.warning(
        f"Warning : An indication that something unexpected happened "
    )
    custom_logger.error(f"Error : Due to a more serious problem ")
    custom_logger.critical(
        f"Critical : A serious error, indicating that the program itself may not be able to contine"
    )

    return HttpResponse("Logging Completed!")


# http://127.0.0.1:8000/djangobasicsapp/IfTagDemo
def iftagdemo(request):
    data = {
        "name": "James Anderson",
        "isVisible": True,
        "loggedIn": False,
        "countryCode": "IN",
        "workExperience": 15,
    }
    templateFilename = "djangobasicsapp/IfTagDemo.html"
    context = {"Data": data}
    return render(request, templateFilename, context=context)


def ShowProducts(request):
    Products = [
        {
            "productID": 1,
            "productName": "AMD Ryzen 3990",
            "quantity": 100,
            "unitsInStock": 50,
            "disContinued": False,
            "cost": 3000,
        },
        {
            "productID": 2,
            "productName": "AMD Ryzen 3980",
            "quantity": 100,
            "unitsInStock": 50,
            "disContinued": False,
            "cost": 4000,
        },
        {
            "productID": 3,
            "productName": "AMD Ryzen 3970",
            "quantity": 100,
            "unitsInStock": 50,
            "disContinued": False,
            "cost": 5000,
        },
        {
            "productID": 4,
            "productName": "AMD Ryzen 3960",
            "quantity": 100,
            "unitsInStock": 50,
            "disContinued": True,
            "cost": 6000,
        },
        {
            "productID": 5,
            "productName": "AMD Ryzen 3950",
            "quantity": 100,
            "unitsInStock": 50,
            "disContinued": False,
            "cost": 7000,
        },
        {
            "productID": 6,
            "productName": "AMD Ryzen 3940",
            "quantity": 100,
            "unitsInStock": 50,
            "disContinued": True,
            "cost": 8000,
        },
        {
            "productID": 7,
            "productName": "AMD Ryzen 3930",
            "quantity": 100,
            "unitsInStock": 50,
            "disContinued": True,
            "cost": 9000,
        },
        {
            "productID": 8,
            "productName": "AMD Ryzen 3920",
            "quantity": 100,
            "unitsInStock": 50,
            "disContinued": False,
            "cost": 10000,
        },
    ]
    Processors = [
        {
            "Category": "AMD",
            "processors": ["Ryzen 3990", "Ryzen 3970", "Ryzen 3960", "Ryzen 3950"],
        },
        {"Category": "Intel", "processors": ["Xeon 8362", "Xeon 8358", "Xeon 8380"]},
    ]

    TemplateFile = "djangobasicsapp/ShowProducts.html"
    context = {
        "Products": Products,
        "TotalProducts": len(Products),
        "Processors": Processors,
    }
    return render(request, TemplateFile, context)


import requests


def LoadUsers(request):
    templatefilename = "djangobasicsapp/ShowUsers.html"
    response = CallRestAPI()
    context = {"users": response.json()}
    return render(request, templatefilename, context)


def LoadUsers2(request):
    templatefilename = "djangobasicsapp/ShowUsersAsCards.html"
    image = "https://i.pravatar.cc"
    response = CallRestAPI()
    context = {"users": response.json(), "image": image}
    return render(request, templatefilename, context)


def CallRestAPI():
    BASE_URL = "https://fakestoreapi.com"
    return requests.get(f"{BASE_URL}/users")


def CallRestAPI2(userid):
    BASE_URL = "https://fakestoreapi.com"
    return requests.get(f"{BASE_URL}/users/{userid}")


def LoadUserDetails(request):
    if request.POST.get("useridcounter") == None:
        counter = 1
    else:
        counter = int(request.POST.get("useridcounter"))
    if request.POST.get("btnNext"):
        counter += 1
        if counter >= 11:
            counter = 1
    elif request.POST.get("btnPrevious"):
        counter -= 1
        if counter == 0:
            counter = 0
    else:
        counter = 1
    templatefilename = "djangobasicsapp/ShowUserDetails.html"
    response = CallRestAPI2(counter)
    image = "https://i.pravatar.cc"
    context = {"user": response.json(), "image": image}
    return render(request, templatefilename, context)
