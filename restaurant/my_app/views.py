from django.shortcuts import render
from django.core.mail import send_mail
# from django.http import HttpResponseRedirect
# from .forms import ContactForm
# Create your views here.
def index(request):
    return render(request,'index.html')

def contact_us(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        subject =request.POST['subject']
        message=request.POST['message']

        # send EMAIL
        send_mail(
            "Restaurant contact "+name, #subject
            message, # message
            email,# from email
            ['nikshhbmsit@gmail.com'],# To email
        )

        return render(request,'index.html', {'name':name})

    else:
        return render(request, 'index.html')


def reservation(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phone =request.POST['phone']
        date =request.POST['date']
        time =request.POST['time']
        people =request.POST['people']
        message=request.POST['message']


        booking = "Name: "+name +" Phone: "+phone + " Date: "+date + " Time: "+time +" People: "+people+" Message: "+message

        # send EMAIL'''
        send_mail(
            "Restaurant Booking request ", #subject
            booking, # message
            email,# from email
            ['nikshhbmsit@gmail.com'],# To email
        )

        return render(request,'reservation.html', {
            'name' : name,
            'email' : email,
            'phone' : phone,
            'date' : date,
            'time' : time,
            'people': people,
            'message' : message
            })

    else:
        return render(request, 'index.html')
