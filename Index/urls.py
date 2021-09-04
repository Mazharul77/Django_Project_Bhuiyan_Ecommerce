from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ABOUT/', views.about_func, name='about_us'),
    path("Mazharul's_Blog", views.blogs, name='blog'),
    path('All/', views.details, name='some_details'),
]