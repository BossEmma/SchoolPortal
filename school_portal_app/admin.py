from django.contrib import admin
from .models import Gallery, Events, Blogs, User, Fee, SchoolSession, Term, Subject, Class


class FeeDisplay(admin.ModelAdmin):
    list_display = ("name", "amount")


class TermDisplay(admin.ModelAdmin):
    list_display = ("term", "session")


# Register your models here.
admin.site.register(Blogs)
admin.site.register(Events)
admin.site.register(Gallery)
admin.site.register(Fee, FeeDisplay)
admin.site.register(Term, TermDisplay)
admin.site.register(SchoolSession)
admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Class)