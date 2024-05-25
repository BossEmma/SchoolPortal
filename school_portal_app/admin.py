from django.contrib import admin
from .models import Gallery, Events, Blogs, Student, Staff, User, Result, Transaction_History, Subject, Class


class StudentDisplay(admin.ModelAdmin):
    list_display = ("full_name", "student_class", "status")


class StaffDisplay(admin.ModelAdmin):
    list_display = ("full_name", "role")


# Register your models here.
admin.site.register(Blogs)
admin.site.register(Events)
admin.site.register(Gallery)


admin.site.register(User)
admin.site.register(Class)
admin.site.register(Result)
admin.site.register(Subject)
admin.site.register(Transaction_History)
admin.site.register(Student, StudentDisplay)

admin.site.register(Staff, StaffDisplay)