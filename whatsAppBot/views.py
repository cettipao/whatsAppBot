from django.shortcuts import render
from django_twilio.decorators import twilio_view
from twilio.twiml.messaging_response import MessagingResponse
from .models import Talker

@twilio_view
def smsView(request):
    number = request.POST.get('From','')
    if number in Talker.objects.all():
        msg = "Bienvenido de Nuevo, intentado conectar..."
    else:
        msg = "Bienvenido, intentado conectar..."
        Talker.objects.create(number)
    name = request.POST.get('Body', '')
    #msg = 'Hey %s, how are you today?' % (name)
    r = MessagingResponse()
    r.message(msg)
    return r