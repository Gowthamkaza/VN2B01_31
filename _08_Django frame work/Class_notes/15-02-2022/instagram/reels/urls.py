from django.urls import path
from .views import *
urlpatterns = [
    path('', some_fun, name = 'harsha'),
    path('myref/<name>', some_fun2, name='myname'),

]
