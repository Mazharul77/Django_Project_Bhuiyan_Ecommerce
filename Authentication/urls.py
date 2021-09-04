from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_func,name='login'),
    path('Registration/',views.registration_func,name='register'),
    path('Forgot_Pass/',views.forgot_func,name='forgotPass'),
    path('Log_Out/',views.logout_func,name='logout'),
]
