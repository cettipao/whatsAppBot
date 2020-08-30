from django.urls import path
from .views import smsView, homeView,downloadView

urlpatterns = [
    path('',homeView),
    path('download/',downloadView),
    path('sms/', smsView),
]