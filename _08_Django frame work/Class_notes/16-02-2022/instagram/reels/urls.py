from django.urls import path
from .views import *
urlpatterns = [
    path('', some_fun, name = 'harsha'),
path('harsha/<str:name>/<int:id>', some_fun2, name = 'ha'),
    path('render_path/', rend_func, name='render'),
    path('render_path/<str:name>/<int:id>', rend_fun2, name='render2'),
path('render_path/main', rend_fun3, name='render3'),
path('render/', post_method, name='post'),

]


# create a view in your views.py
# create a html if it is needed
# create url path