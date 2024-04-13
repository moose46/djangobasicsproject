from django.urls import path

from . import views

urlpatterns = [
    path("Home", views.Home, name="Home"),
    path("", views.Home, name="Home"),
    path("ShowMessages", views.ShowMoreMessage, name="ShowMessages"),
    path("UseVariables", views.UseVariablesAsResponse, name="UVR"),
    path("GetRequestDemo", views.GetRequestVariables, name="GVR"),
    path("ShowTime", views.ShowDateTimeInfo, name="SDI"),
    path("LoggingDemo", views.LogginExample, name="LoggingExample"),
    path("IfTagDemo", views.iftagdemo, name="ITD"),
    path("ShowProducts", views.ShowProducts, name="SP"),
]
