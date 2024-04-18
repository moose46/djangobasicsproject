from django.urls import path

from . import views

urlpatterns = [
    path("Home", views.Home, name="Home"),
    path("", views.Index, name="Index"),
    path("Index", views.Index, name="Index"),
    path("ShowMessages", views.ShowMoreMessage, name="ShowMessages"),
    path("UseVariables", views.UseVariablesAsResponse, name="UVR"),
    path("GetRequestDemo", views.GetRequestVariables, name="GVR"),
    path("ShowTime", views.ShowDateTimeInfo, name="SDI"),
    path("LoggingDemo", views.LogginExample, name="LoggingExample"),
    path("IfTagDemo", views.iftagdemo, name="ITD"),
    path("ShowProducts", views.ShowProducts, name="SP"),
    path("ShowUsers", views.LoadUsers, name="LU"),
    path("ShowUsers2", views.LoadUsers2, name="LU2"),
    path("ShowUsersDetails", views.LoadUserDetails, name="ShowUserDetails"),
    path("PassModel", views.PassModelToTemplate, name="PassModel"),
    path("BIFDemo", views.BuiltInFiltersDemo, name="BIF"),
    path("CustomFiltersDemo", views.CustomFiltersDemo, name="CFDemo"),
    path("TestStaticFiles", views.TestStaticFiles, name="TSF"),
]
