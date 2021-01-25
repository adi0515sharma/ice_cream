from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('index', views.index, name='Home'),
    path("about",views.about,name="about"),
    path("blog",views.blog,name="blog"),
    path("contact",views.contact,name="contact"),
    path("singlepost",views.singlepost,name="singalpost"),
    
    path("product",views.product,name="product")
]
