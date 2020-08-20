from django.shortcuts import render
from twilio.twiml.messaging_response import MessagingResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def smsView(request, *args, **kwargs):
    msg = request.POST.get('body')
    resp = MessagingResponse()
    resp.message("You said: {}".format(msg))
    return HttpResponse(resp.to_xml(), content_type='text/xml')
