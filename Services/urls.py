from django.urls import path
from . import views

urlpatterns = [

    path('', views.design_develop, name='Web_DD'),
    path('software_Solution/', views.soft_solve, name='Software'),
    path('Mobile_App_API_Integration/', views.app_api_integration, name='appAPI'),
]