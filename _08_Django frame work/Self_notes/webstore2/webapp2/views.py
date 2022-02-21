from django.shortcuts import render,redirect
from django import forms
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def func1(request):
    return HttpResponse("This is Gowtham")


def func2(request):
    return render(request,"webapp2/first.html")


def func3(request,name,age):
    data={'keyname':name,'keyage':age}
    return render(request,"webapp2/second.html",data)


def func4(request):
    names={'gowtham,''uday','basi'}
    loc={'bangalore','hyderabad','Guntur'}
    id={1,2,3,4,5}
    Data2={'keyname':names,'keyloc':loc,'keyid':'id'}
    return render(request,"webapp2/thirdfile.html",Data2)
def home2(request):
    return render(request,"fourthfile.html",{"name":"gowtham"})
def addreq(request):
    val1=int(request.GET.get["num1"])
    val2= int(request.GET.get["num2"])
    res=val1+val2
    return render(request,"fourthfile.html",{"result":res})

def post_method(request):
    if request.method == "POST":
        form = addreq(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = addreq()
    return render(request, 'index.html', {'form': form})





