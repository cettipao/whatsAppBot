from django.urls import path
from .views import smsView, homeView

urlpatterns = [
    path('',homeView),
    path('sms/', smsView),
]