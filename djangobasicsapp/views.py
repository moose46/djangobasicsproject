import datetime
import http
from mailbox import Message

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# function based view
# http://127.0.0.1:8000/djangobasicsapp/Home
def Home(request):
    return HttpResponse("<h1>Hello World! Django 5.0.4</h1>")


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
