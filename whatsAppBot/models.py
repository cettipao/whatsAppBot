from django.db import models

# Create your models here.


class Talker(models.Model):
    number = models.CharField(max_length=30)
    dateCreated = models.DateField(auto_now=True)
