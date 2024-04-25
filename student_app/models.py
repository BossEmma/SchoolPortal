from django.db import models
from django.core.validators import MaxValueValidator

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

JSS_SUBJECTS = [
    ('Mathematics', 'Mathematics'),
    ('English', 'English'),
]

SSS_SCIENCE_SUBJECTS = [
    ('Physics', 'Physics'),
    ('Chemistry', 'Chemistry'),
]

SSS_ART_SUBJECTS = [
    ('Physics', 'Physics'),
    ('Chemistry', 'Chemistry'),
]


class StudentProfile(models.Model):
    first_name = models.CharField(("First Name"), max_length=100, blank=True, null=True)
    other_name = models.CharField(("Other Name"), max_length=100, blank=True, null=True)
    last_name = models.CharField(("Last Name"), max_length=100, blank=True, null=True)
    email_address = models.CharField(("Email Address"), max_length=100, blank=True, null=True)
    phone_number = models.CharField(("Phone Number"), max_length=100, blank=True, null=True)
    age = models.PositiveIntegerField(("Age"), validators=[MaxValueValidator(50)], blank=True, null=True)
    student_class = models.CharField(("Class"), choices=STUDENT_CLASS, max_length=50, null=True)
    status= models.CharField(("Status"), max_length=100, choices=STATUS, blank=True, null=True)
    subjects = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True, blank=True, related_name='students')

    @property
    def full_name(self):
        return f"{self.first_name} {self.other_name} {self.last_name}"  

    def __str__(self):
        return self.full_name
    

class Subject(models.Model):
    name = models.CharField(("Subject Name"), max_length=100, null=True)
    student_class = models.CharField(("Class"), choices=STUDENT_CLASS, max_length=50, null=True)

    def __str__(self):
        return self.name


class Result(models.Model):
    student = models.ForeignKey(("StudentProfile"), on_delete=models.CASCADE, related_name='results')
    subject = models.ForeignKey(("Subject"), on_delete=models.CASCADE, related_name='results')
    score = models.DecimalField(("Score"), max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.student.full_name} - {self.subject.name} - Score: {self.score}"


#TRANSACTION MODEL"""