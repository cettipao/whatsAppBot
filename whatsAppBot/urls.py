from django.urls import path,include
from .views import smsView

urlpatterns = [
    path('', smsView, name='sms'),
]