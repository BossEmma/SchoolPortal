from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator
# Create your models here.


class StaffProfile(models.Model):
    first_name= models.CharField(("First Name"), max_length=100, null=True)
    other_name= models.CharField(("Other Name"), max_length=100, null=True)
    last_name= models.CharField(("Last Name"), max_length=100, null=True)
    email_address= models.CharField(("Email Address"), max_length=100, null=True)
    phone_number= models.CharField(("Phone Number"), max_length=100, null=True)
    age= models.PositiveIntegerField(("Age"), validators=[MaxValueValidator(50)], null=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.other_name} {self.last_name}"  

    def __str__(self):
        return self.full_name
