from django.shortcuts import render
from .models import Contact

# Create your views here.
def contact_func(request):
    phone = +8801515267787
    # return HttpResponse(phone)

    info={
        'name': 'Mazharul',
        'email': 'mazharul15-1425@diu.ed.bd',
        'phone': '+880 15 15 26 77 87',
        'age': 24,
        'fb': 'mazharul.---'
    }

    if request.method=='POST':
        name= request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_info = Contact(name = name, email = email, subject = subject, message = message)
        contact_info.save()


    return render(request,'contact.html', info)
