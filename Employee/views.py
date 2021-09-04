from django.http import HttpResponse
from django.shortcuts import render
# from django.contrib.auth import authenticate, logout

def employee(request):
    return HttpResponse("This is EMPLOYEE page")

    
def designation(request):
    return render(request, 'employee/designation.html')

