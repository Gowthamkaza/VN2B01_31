from django.shortcuts import render, HttpResponse

def some_fun(request):
    return HttpResponse("Hello Harsha")

def some_fun2(request,name,id):
    return HttpResponse('Hello {} your id is {}'.format(name,id))

def rend_func(request):
    return render(request,'reels/index.html')

def rend_fun2(request,name,id):
    data = {'key_name':name,'key_id':id}
    return render(request,'reels/main.html',data)

def rend_fun3(request):
    names = ['harsha','ranjith','mani','madhu']
    locations = [ 'blr','hyd']
    ids = [1,2,3,4]
    data = {'key_names':names,'key_locations':locations,'key_ids':ids}
    return render(request,'reels/main2.html',data)