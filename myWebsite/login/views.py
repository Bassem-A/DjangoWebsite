from django.http import HttpResponse
from django.shortcuts import render
from .models import User


# Create your views here.

def index(request):

    return render(request, "login/index.html",{

        "Usernames": User.objects.all()


    })