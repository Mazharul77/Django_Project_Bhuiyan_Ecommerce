from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def design_develop(request):
    material={
    'design_names': ['Design Website', 'Responsive Web Design',
    'Develop & Beautify Web App', 'HTML','CSS', 'Boot Strap', 'Reat-Js', 'Django Based Sites']
    }

    return render(request, 'services/services.html', material)
    

def soft_solve(request):
    return render(request, 'services/softSolution.html')

def app_api_integration(request):
    return render(request, 'services/appAPI.html')
