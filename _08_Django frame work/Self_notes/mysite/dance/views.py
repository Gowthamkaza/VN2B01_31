from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request,username ):
    return HttpResponse("This is the profile page! the user is {}".format(username))

def rend_func(request):
    return render(request,"reels2/first_file.html")

def rend_func2(request,name,age):
    data={'keyname':name,'keyage':age}
    return render(request,"reels2/second_file.html",data)

def rend_func3(request):
    names={'gowtham,''uday','basi'}
    loc={'bangalore','hyderabad','Guntur'}
    id={1,2,3,4,5}
    Data2={'keyname':names,'keyloc':loc,'keyid':'id'}
    return render(request,"reels2/third_file.html",Data2)
