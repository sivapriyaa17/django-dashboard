from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    type_choices=[("patient","patient"),("doctor","doctor"),]
    type=models.CharField(choices=type_choices,max_length=20)
    profile=models.ImageField(upload_to='profile/',null=True,blank=True)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.CharField(max_length=15)
    def __str__(self):
        return self.username+" "
    

# Create your models here.
