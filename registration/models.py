from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Registration(models.Model):
    firstname = models.TextField(max_length=100,default='')
    moiddlename = models.TextField(max_length=100,default='')
    lastname = models.TextField(max_length=100,default='')
    age = models.TextField(max_length=100,default='0')
    gender = models.TextField(max_length=100,default='')
    client_id = models.TextField(max_length=10,default='')
    mobile = models.TextField(max_length=15,default='0xxx')
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) :
        return self.mobile
