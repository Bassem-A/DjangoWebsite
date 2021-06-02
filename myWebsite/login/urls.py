from django.urls import path

from . import views

urlpatterns = [

    #path("", views.User, name="LoginPage")
    path("", views.index, name="index")


]