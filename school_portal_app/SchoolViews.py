from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Gallery
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


school_name = "Noble Academy"
school_slogan = "Society for Positive Living"

school_email= "contact@school.com"
school_phone1= "2203332023"
school_phone2= "239777337"
school_address= ""


# Create your views here.

def handler404(request, exception):
    return HttpResponseRedirect('home')

def error(request):
    return render(request, "school/error.html")

def SendEmail(x, y, z):
    pass

def home(request):
    gallery= Gallery.objects.all()
    
    context = {
        'school_name': school_name,
        'school_slogan': school_slogan,

        'gallery': gallery,
    }
    return render(request, "school/index.html", context)


def academic_info(request):
    return render(request, "school/academic-information.html")

def admission_notice(request):
    return render(request, "school/admission-notices.html")

def blog(request):
    return render(request, "school/our-blog.html")

def blog_details(request):
    return render(request, "school/blog-details.html")

def vision(request):
    return render(request, "school/vision-mission-objectives.html")

def gallery(request):
    return render(request, "school/gallery.html")

def event(request):
    return render(request, "school/event.html")

def event_details(request):
    return render(request, "school/event-details.html")

def contact(request):
    return render(request, "school/contact.html")

def history(request):
    return render(request, "school/history.html")

def message(request):
    return render(request, "school/message.html")

def objective(request):
    return render(request, "school/objectives-detail.html")

def resources(request):
    return render(request, "school/resources&facilities.html")

def service(request):
    return render(request, "school/service.html")

def staffs(request):
    return render(request, "school/staff&members.html")

def about(request):
    return render(request, "school/who-we-are.html")



#@login_required(login_url='/accounts/login/')
def sign_out(request):
    logout(request)
    return redirect("home")
