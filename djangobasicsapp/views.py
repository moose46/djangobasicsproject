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
