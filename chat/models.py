from datetime import datetime
from django.db import models

# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=100)

class Message(models.Model):
    value = models.CharField(max_length=100000)
    date = models.DateField(default=datetime.now,blank=True)
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=100)