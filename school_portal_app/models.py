from django.db import models
from django.core.validators import MaxValueValidator
from staff_app.models import StaffProfile 
# Create your models here.




class Gallery(models.Model):
    name = models.CharField(("Name"), max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Gallery"

    def __str__(self):
        return self.name
    
class Events(models.Model):
    title = models.CharField("Name", max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    summary = models.CharField("Summary", max_length=100, blank=True, null=True)
    date = models.CharField("Date", max_length=100, blank=True, null=True)


    address = models.CharField("Address", max_length=100, blank=True, null=True)
    phone = models.CharField("Phone", max_length=100, blank=True, null=True)
    time = models.CharField("Time", max_length=100, blank=True, null=True)
    #hosts=

    class Meta:
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title

