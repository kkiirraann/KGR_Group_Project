from django.db import models
from django.utils import timezone

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length = 50, default = 'Guest User')
    phone_num = models.IntegerField(default = 1234)
    email_id = models.CharField(max_length = 50, default = '')
    password = models.CharField(max_length = 30, default = 'pass1234')
    address = models.CharField(max_length = 50, default = 'Hyderabad')
    date_created = models.DateField(default = timezone.now)
    status = models.BooleanField(default = True)
    order_id = models.CharField(max_length = 25, default = '')

    def __str__(self):
        return self.name