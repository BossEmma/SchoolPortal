from django.contrib import admin
from .models import Student, Result, Transaction_History, SubjectResult


class StudentDisplay(admin.ModelAdmin):
    list_display = ("full_name", "student_class", "status")



# Register your models here.


admin.site.register(Result)
admin.site.register(SubjectResult)
admin.site.register(Transaction_History)
admin.site.register(Student, StudentDisplay)