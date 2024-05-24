from django.contrib import admin
from .models import Gallery, Events, Blogs, StudentProfile, StaffProfile, User


#class MovieDisplay(admin.ModelAdmin):
#    list_display = ("title", "rating", "download")


# Register your models here.

admin.site.register(User)
admin.site.register(Gallery)
admin.site.register(Events)
admin.site.register(Blogs)
admin.site.register(StudentProfile)
admin.site.register(StaffProfile)