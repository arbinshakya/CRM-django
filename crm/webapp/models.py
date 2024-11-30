from django.db import models
from django.contrib.auth.models import User

class Record(models.Model):

    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length= 255)
    last_name  = models.CharField(max_length= 255)
    email = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 20)
    address = models.CharField(max_length= 255)
    city = models.CharField(max_length= 255)
    province = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)

    def __str__ (self):
        return self.first_name + " " + self.last_name