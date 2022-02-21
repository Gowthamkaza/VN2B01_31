from django.urls import path
from . import views

urlpatterns=[
    path('type/',views.func1, name='gowtham'),
    path('',views.func2),
    path('checking/<name>/<age>',views.func3),
    path('checks/',views.func4),
    path('see/',views.home2),
    path('watch/',views.addreq),
    path('see/',views.post_method)
]