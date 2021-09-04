
from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.employee),
    path('designation/',views.designation, name='Emp.desig')
    
    
]