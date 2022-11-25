from multiprocessing.sharedctypes import Value
from django.db import models
from ast import Delete
from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.forms import NumberInput, PasswordInput, TextInput
from django.core.validators import MaxValueValidator

# Create your models here.
class User(AbstractUser):
    pass 
    


class UserInf(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    father_name = models.CharField(TextInput, max_length = 30)
    national_code = models.IntegerField(NumberInput,validators=[MaxValueValidator(9999999999)])
    phone_number = models.IntegerField(NumberInput,validators=[MaxValueValidator(999999999999)])
    address = models.TextField(max_length = 100,blank=True)
 
    def __str__(self):
        return f"username:{self.username},father_name:{self.father_name}"

class Doctors(models.Model):
    specialty   = models.CharField(TextInput, max_length = 64)
    doctor_name = models.CharField(TextInput, max_length = 64)
    capacity = models.IntegerField(default=30,null=True,blank=True)

    mandeh = models.IntegerField(default=30, null=True,blank=True)
    nobat = models.PositiveIntegerField(default=1)

    time = models.TimeField(null=True)
    date = models.DateField(null=True)
    is_active = models.BooleanField(default = False,null=True)
    is_end = models.BooleanField(default = False)

    def __str__(self):
        return f"specialty:{self.specialty} -- doctor_name:{self.doctor_name}"

    def serialize(self):
        return {
            "id": self.id,
            "specialty":self.specialty,
            "doctor_name": self.doctor_name,
            "date" : self.date,
            "time": self.time,
            "capacity": self.capacity,
            "mandeh": self.mandeh
        }

class Reserve(models.Model):
    username = models.ForeignKey(UserInf, on_delete = models.CASCADE,blank =True,null=True)
    inf_turn = models.ManyToManyField(Doctors,blank=True)

    
 
    def __str__(self):
        return f"username:{self.username}; Doctors-information: ..."

    


    

