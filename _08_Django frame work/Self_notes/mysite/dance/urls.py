from django.urls import path

from . import views

urlpatterns=[
    path('type/<str:username>',views.home),
    path('check/',views.rend_func),
    path('checks/<name>/<age>',views.rend_func2),
    path('checks/',views.rend_func2),
    path('checking/',views.rend_func3)
]