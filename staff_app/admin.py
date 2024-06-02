from django.contrib import admin
from .models import Staff

class StaffDisplay(admin.ModelAdmin):
    list_display = ("full_name", "role")


# Register your models here.
admin.site.register(Staff, StaffDisplay)