from django.shortcuts import render, HttpResponse

def some_fun(request):
    return HttpResponse("Hello Harsha")


def some_fun2(request,name):
    return HttpResponse(f"Hello {name}")
# Create your views here.
#127.0.0.1:8000/