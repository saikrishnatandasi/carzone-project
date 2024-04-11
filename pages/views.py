from django.shortcuts import render,redirect
from .models import Team
from cars.models import Car
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages



# Create your views here.
def home(request):
    teams = Team.objects.all()
    feautred_cars = Car.objects.order_by('-created_date').filter(is_featured = True)
    all_cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat = True).distinct()
    year_search = Car.objects.values_list('year', flat = True).distinct()
    city_search = Car.objects.values_list('city',flat = True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat = True).distinct()
    data = {
     'teams': teams,
     'feautred_cars': feautred_cars,
     'all_cars': all_cars,
     'model_search': model_search,
     'year_search': year_search,
     'city_search': city_search,
     'body_style_search': body_style_search,

    }
    return render(request,'pages/home.html',data)

def about(request):
    teams = Team.objects.all()
    data = {
     'teams':teams,
    }
    return render(request, 'pages/about.html',data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message from Car Zone Website regarding " '+ subject + '"'
        message_body = "Name: "+ name + "\nEmail: "+ email + "\nPhone: " + phone + "\nMessage : " +message

        admin_info = User.objects.get(is_superuser = True)
        admin_email = admin_info.email

        send_mail(
            email_subject,
            message_body,
            "saikrishna240801@gmail.com",
            [admin_email],
            fail_silently=False,
            )
        messages.success(request, 'Thank You for Contacting. We will get back shortly')
        return redirect('contact')
    return render(request, 'pages/contact.html')
