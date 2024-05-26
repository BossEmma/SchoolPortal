from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
import random, string



# Create your models here.

class Announcement(models.Model):
    title= models.CharField("Title", max_length=100, blank=True, null=True)
    date= models.DateTimeField("Date", auto_now_add=True)
    announcement= models.TextField("Announcement", max_length=2000, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Announcements"
        ordering = ['date']

    def __str__(self):
        return self.title
    

class Gallery(models.Model):
    name = models.CharField("Name", max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Gallery"

    def __str__(self):
        return self.name
    
class Events(models.Model):
    title = models.CharField("Name", max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    summary = models.CharField("Summary", max_length=100, blank=True, null=True)
    date = models.DateTimeField("Date",  auto_now=False, auto_now_add=False, blank=True, null=True)

    address = models.CharField("Address", max_length=100, blank=True, null=True)
    phone = models.CharField("Phone", max_length=100, blank=True, null=True)
    time = models.TimeField("Time", auto_now=False, auto_now_add=False, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title

    
class Blogs(models.Model):
    title = models.CharField("Name", max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    summary = models.CharField("Summary", max_length=100, blank=True, null=True)
    date = models.DateTimeField(("Date"), auto_now_add=True)
    blog = models.TextField("Blog", max_length=2000, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Blogs"
        ordering = ['title']

    def __str__(self):
        return self.title
    

"""Trer = [
    ('JSS 1', 'JSS 1'),
    ('JSS 2', 'JSS 2'),
    ('JSS 3', 'JSS 3'),
    ('SSS 1', 'SSS 1'),
    ('SSS 2', 'SSS 2'),
    ('SSS 3', 'SSS 3')
]"""


class SchoolSession(models.Model):
    name = models.CharField(max_length=100, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Term(models.Model):
    name = models.CharField(max_length=100)
    session = models.ForeignKey(SchoolSession, related_name='terms', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.session.name})"



#USERS
    
class UserManager(BaseUserManager):
    def create_user(self, surname, password=None, **extra_fields):
        if not surname:
            raise ValueError('The Surname field must be set')
        user = self.model(surname=surname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, surname, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(surname, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(("First Name"), max_length=100, blank=True, null=True)
    middle_name = models.CharField(("Other Name"), max_length=100, blank=True, null=True)
    surname = models.CharField(("Surname"), max_length=100, blank=True, null=True, unique=True)
    age = models.PositiveIntegerField(("Age"), validators=[MaxValueValidator(50)], blank=True, null=True)
    #sex
    phone_number = models.CharField(("Phone Number"), max_length=100, blank=True, null=True)
    phone_number2 = models.CharField(("Phone Number 2"), max_length=100, blank=True, null=True)
    passport = models.ImageField(upload_to='images/', blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'surname'
    REQUIRED_FIELDS = ['first_name', 'middle_name', 'email', 'age', 'phone_number']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.middle_name} {self.surname}"  
    


#Student Models
STUDENT_CLASS = [
    ('JSS 1', 'JSS 1'),
    ('JSS 2', 'JSS 2'),
    ('JSS 3', 'JSS 3'),
    ('SSS 1', 'SSS 1'),
    ('SSS 2', 'SSS 2'),
    ('SSS 3', 'SSS 3')
]

STATUS = [
    ('Ongoing', 'Ongoing'),
    ('Graduate', 'Graduate'),
    ('Suspended', 'Suspended'),
    ('Expelled', 'Expelled'),
]

SUBJECTS = [
    #Basic Subjects
    ('Mathematics', 'Mathematics'),
    ('English Language', 'English Language'),

    #Junior Secondary School
    ('Basic Science', 'Basic Science'),
    ('Social Studies', 'Social Studies'),
    ('Fine Arts', 'Fine Arts'),
    ('Agricultural Science', 'Agricultural Science'),
    ('Civic Education', 'Civic Education'),
    ('Christian Religion Studies', 'Christian Religion Studies'),
    ('Physical and Health Education', 'Physiacal and Health Education'),
    ('Business Studies', 'Business Studies'),
    ('Computer Science', 'Computer Science'),
    ('Home Economics', 'Home Economics'),
    ('Basic Technology', 'Basic Technology'),
    
    #`SSS Science Subjects
    ('Biology', 'Biology'),
    ('Physics', 'Physics'),
    ('Chemistry', 'Chemistry'),
    ('Further Mathematics', 'Further Mathematics'),


    # SSS Arts Subjects
    ('Food and Nutrition', 'Food and Nutrition'),
    ('Finance Account', 'Finance Account'),
    ('Commerce', 'Commerce'),

    ('Economics', 'Economics'),
    ('Government', 'Government'),

    ('Literature in English', 'Literature in English'),
    ('Geography', 'Geography'),
]

TRANSACTION_STATUS= [
    ('PENDING', 'PENDING'),
    ('SUCCESS', 'SUCCESS')
]

class Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    student_class = models.ForeignKey("Class", on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    status= models.CharField("Status", max_length=100, choices=STATUS, blank=True, null=True)

    def __str__(self):
        return self.user.full_name
    
    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.middle_name} {self.user.surname}" 
    


class Subject(models.Model):
    name = models.CharField(("Subject Name"), choices=SUBJECTS, max_length=100, null=True)

    def __str__(self):
        return self.name
    

class Class(models.Model):
    name= models.CharField(("Class"), choices=STUDENT_CLASS, max_length=100, blank=True, null=True)
    subjects = models.ManyToManyField(Subject, blank=True)

    def __str__(self):
        return self.name


class Result(models.Model):
    student = models.ForeignKey(("Student"), on_delete=models.CASCADE, related_name='results')
    subject = models.ForeignKey(("Subject"), on_delete=models.CASCADE, choices=STATUS, related_name='subjects')
    score = models.DecimalField(("Score"), max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.student.full_name
    


class Transaction_History(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount= models.IntegerField(("Paid Balance"), blank= True, validators=[MaxValueValidator(9999999999)])
    timestamp= models.DateTimeField(("Date"), auto_now_add=True)
    status= models.CharField(("Payment Status"), choices=TRANSACTION_STATUS, max_length= 50)
    method= models.CharField(("Payment Method"), max_length= 50)

    def __str__(self):
        return self.student.full_name




# Staff Models
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
    