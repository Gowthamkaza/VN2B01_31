from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request,username ):
    return HttpResponse("<h1>This is the profile page! the user is {}.</h1>".format(username))

