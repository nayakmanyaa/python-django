from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable": "this is sent"
    }
    messages.success(request, "test msg")
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")


def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is services page")



def contact(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        city = request.POST.get('city')
        gender = request.POST.get('gender')
        about = request.POST.get('about')
        contact = Contact(firstname=firstname, lastname=lastname, email=email, city=city, gender=gender, mobile=mobile, about=about, date=datetime.today())
        contact.save()
    return render(request, 'contact.html')
    messages.success(request, 'Your message have been sent.')
    # return HttpResponse("this is contact page")
    
    
