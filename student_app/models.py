"""from django.db import models
from django.core.validators import MaxValueValidator

STUDENT_CLASS = [
    ('JSS 1', 'JSS 1'),
    ('JSS 2', 'JSS 2'),
    ('JSS 3', 'JSS 3'),
    ('SSS 1', 'SSS 1'),
    ('SSS 2', 'SSS 2'),
    ('SSS 3', 'SSS 3')
]

# Example subject lists
JSS_SUBJECTS = [
    ('Mathematics', 'Mathematics'),
    ('English', 'English'),
    # Add more subjects as needed
]

SSS_SUBJECTS = [
    ('Physics', 'Physics'),
    ('Chemistry', 'Chemistry'),
    # Add more subjects as needed
]

class StudentProfile(models.Model):
    first_name = models.CharField(("First Name"), max_length=100, null=True)
    other_name = models.CharField(("Other Name"), max_length=100, null=True)
    last_name = models.CharField(("Last Name"), max_length=100, null=True)
    email_address = models.CharField(("Email Address"), max_length=100, null=True)
    phone_number = models.CharField(("Phone Number"), max_length=100, null=True)
    age = models.PositiveIntegerField(("Age"), validators=[MaxValueValidator(50)], null=True)
    student_class = models.CharField(("Class"), choices=STUDENT_CLASS, max_length=50, null=True)
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
    student = models.ForeignKey('StudentProfile', on_delete=models.CASCADE, related_name='results')
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='results')
    score = models.DecimalField(("Score"), max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.student.full_name} - {self.subject.name} - Score: {self.score}"


#TRANSACTION MODEL"""