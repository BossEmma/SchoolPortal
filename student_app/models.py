from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator
from school_portal_app.models import User, Term, Class, Subject


# Create your models here.



#Student Models


STATUS = [
    ('Ongoing', 'Ongoing'),
    ('Graduate', 'Graduate'),
    ('Suspended', 'Suspended'),
    ('Expelled', 'Expelled'),
]



TRANSACTION_STATUS= [
    ('PENDING', 'PENDING'),
    ('SUCCESS', 'SUCCESS')
]

class Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    student_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)
    status= models.CharField("Status", max_length=100, choices=STATUS, blank=True, null=True)

    def __str__(self):
        return self.user.full_name
    
    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.middle_name} {self.user.surname}" 
    

STUDENT_CLASS = [
    ('JSS 1', 'JSS 1'),
    ('JSS 2', 'JSS 2'),
    ('JSS 3', 'JSS 3'),
    ('SSS 1', 'SSS 1'),
    ('SSS 2', 'SSS 2'),
    ('SSS 3', 'SSS 3')
]

TERMS= [
    ('1st Term', '1st Term'),
    ('2nd Term', '2nd Term'),
    ('3rd Term', '3rd Term'),
]


class SubjectResult(models.Model):
    student = models.ForeignKey(("Student"), on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    ca_score = models.DecimalField(("C.A Score"), max_digits=5, decimal_places=2, null=True, blank=True)
    test_score = models.DecimalField(("Test Score"), max_digits=5, decimal_places=2, null=True, blank=True)
    exam_score = models.DecimalField(("Exam Score"), max_digits=5, decimal_places=2, null=True, blank=True)
    term= models.CharField("Term", choices=TERMS, max_length=8, null=True, blank=True)
    student_class= models.CharField("Class", choices=STUDENT_CLASS, max_length= 50, null=True, blank=True)
    session= models.CharField("Session", max_length=9, null=True, blank=True)

    def __str__(self):
        return self.student.full_name

    @property
    def total_score(self):
        return self.ca_score + self.test_score + self.exam_score
    
    @property
    def grade(self):
        if self.total_score >= 70:
            return "A"
        elif self.total_score >= 60:
            return "B"
        elif self.total_score >= 50:
            return "C"
        elif self.total_score >= 45:
            return "D"
        elif self.total_score >= 40:
            return "E"
        else:
            return "F"


class Result(models.Model):
    student = models.ForeignKey(("Student"), on_delete=models.CASCADE)
    subject_results= models.ManyToManyField(SubjectResult, blank=True)
    term= models.CharField("Term", choices=TERMS, max_length=8, null=True, blank=True)
    student_class= models.CharField("Class", choices=STUDENT_CLASS, max_length= 50, null=True, blank=True)
    session= models.CharField("Session", max_length=9, null=True, blank=True)

    def __str__(self):
        return self.student.full_name
    


class Transaction_History(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount= models.IntegerField(("Paid Balance"), blank= True, validators=[MaxValueValidator(9999999999)])
    timestamp= models.DateTimeField(("Date"), auto_now_add=True)
    status= models.CharField(("Payment Status"), choices=TRANSACTION_STATUS, max_length= 50, null=True, blank=True)
    method= models.CharField(("Payment Method"), max_length= 50, null=True, blank=True)
    term= models.ForeignKey(Term, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.student.full_name
