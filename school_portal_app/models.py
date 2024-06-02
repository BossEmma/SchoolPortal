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
    

TERMS= [
    ('1st Term', '1st Term'),
    ('2nd Term', '2nd Term'),
    ('3rd Term', '3rd Term'),
]


class SchoolSession(models.Model):
    session= models.CharField("Session", max_length=100, unique=True)

    def __str__(self):
        return self.session


class Term(models.Model):
    term= models.CharField(("Sex"), choices=TERMS, max_length=100, blank=True, null=True)
    session= models.ForeignKey("SchoolSession", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.term


class Fee(models.Model):
    name = models.CharField(max_length=100)
    amount= models.ForeignKey(SchoolSession, related_name='terms', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


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
class Subject(models.Model):
    name = models.CharField(("Subject Name"), choices=SUBJECTS, max_length=100, null=True)

    def __str__(self):
        return self.name
    

STUDENT_CLASS = [
    ('JSS 1', 'JSS 1'),
    ('JSS 2', 'JSS 2'),
    ('JSS 3', 'JSS 3'),
    ('SSS 1', 'SSS 1'),
    ('SSS 2', 'SSS 2'),
    ('SSS 3', 'SSS 3')
]
class Class(models.Model):
    name= models.CharField(("Class"), choices=STUDENT_CLASS, max_length=100, blank=True, null=True)
    subjects = models.ManyToManyField(Subject, blank=True)

    def __str__(self):
        return self.name



GENDER= [
    ('Male', 'Male'),
    ('Female', 'Female'),    
]
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    email= models.EmailField(unique=True)
    first_name= models.CharField(("First Name"), max_length=100, blank=True, null=True)
    middle_name= models.CharField(("Other Name"), max_length=100, blank=True, null=True)
    surname= models.CharField(("Surname"), max_length=100, blank=True, null=True, unique=True)
    age= models.PositiveIntegerField(("Age"), validators=[MaxValueValidator(50)], blank=True, null=True)
    gender= models.CharField(("Sex"), choices=GENDER, max_length=100, blank=True, null=True)
    phone_number = models.CharField(("Phone Number"), max_length=100, blank=True, null=True)
    phone_number2 = models.CharField(("Phone Number 2"), max_length=100, blank=True, null=True)
    passport = models.ImageField(upload_to='images/', blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'surname', 'middle_name', 'age', 'phone_number', 'gender']

    objects = UserManager()

    @property
    def full_name(self):
        return f"{self.first_name} {self.middle_name} {self.surname}"  
    
    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser