from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator
from school_portal_app.models import User


# Create your models here.


STAFF_ROLE = [
    ('Form Teacher', 'Form Teacher'),
    ('Teacher', 'Teacher'),
    ('Bursary', 'Bursary'),
]

class Staff(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, blank=True, null=True)
    role=  models.CharField(("Staff Role"), choices=STAFF_ROLE, max_length=50, null=True)
    salary= models.IntegerField(("Salary Amount"), blank= True, validators=[MaxValueValidator(9999999999)])
    bank= models.CharField(("Staff Role"), choices=STAFF_ROLE, max_length=50, null=True)
    account_number= models.CharField(("Staff Role"), choices=STAFF_ROLE, max_length=50, null=True)

    def __str__(self):
        return self.user.full_name
    
    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.middle_name} {self.user.surname}" 