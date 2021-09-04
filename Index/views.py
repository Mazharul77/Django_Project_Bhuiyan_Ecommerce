from django.shortcuts import render
from django.http import HttpResponse

from .models import About, client_detail
from .models import slider_display


def home(request):
    #return HttpResponse("Welcome to The Main Home")
    about_info = About.objects.all()[0]
    slider_display_info = slider_display.objects.all()
    client_info = client_detail.objects.all()
    context_dict = {
        'about_keys': about_info,
        'slider_display_keys': slider_display_info,
        'client_keys': client_info,
    }
    return render(request,'index.html',context_dict)

def details(request):
    data = "Lorem Ipsum Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...There is no one who loves pain itself, who seeks after it and wants to have it, simply because it is pain..."
    # return HttpResponse(data)
    return render(request,'layouts.html')

def about_func(request):
    # return HttpResponse("This is About page.")
    return render(request,'about.html') 

    
def blogs(request):
    return render(request,'blog.html')

# def blogs(request):
#     return render(request,'display.html')

