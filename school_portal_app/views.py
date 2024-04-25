from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Gallery



school_name = "Noble Academy"
school_slogan = "Society for Positive Living"
school_overview = "jiqncicqehc qh he"
school_about = "iecfnuiqecber cjkerbcieilje"
school_admission_requirements= ["dicn", "idwedjon","piwojne"]
# Create your views here.

def handler404(request, exception):
    return render(request, "error.html")

def SendEmail(x, y, z):
    pass

def home(request):
    gallery= Gallery.objects.all()
    
    context = {
        'school_name': school_name,
        'school_slogan': school_slogan,
        'school_overview': school_overview,
        'school_about': school_about,
        'school_admission_requirements': school_admission_requirements,
        'gallery': gallery,
    }
    return render(request, "index.html", context)


def academic_info(request):
    return render(request, "academic-information.html")

def admission_notice(request):
    return render(request, "admission-notices.html")

def blog(request):
    return render(request, "our-blog.html")

def blog_details(request):
    return render(request, "blog-details.html")

def vision(request):
    return render(request, "vision-mission-objectives.html")

def gallery(request):
    return render(request, "gallery.html")

def event(request):
    return render(request, "event.html")

def event_details(request):
    return render(request, "event-details.html")

def contact(request):
    
    if request.method== "POST":
        sender_name= request.POST["sender_name"]
        sender_email= request.POST["sender_email"]
        message= request.POST["message"]
        SendEmail(sender_name, sender_email, message)
    
    return render(request, "contact.html")

def history(request):
    return render(request, "history.html")

def message(request):
    return render(request, "message.html")

def news(request):
    return render(request, "news.html")

def objective(request):
    return render(request, "objectives-detail.html")

def resources(request):
    return render(request, "resources&facilities.html")

def service(request):
    return render(request, "service.html")

def staffs(request):
    return render(request, "staff&members.html")

def about(request):
    return render(request, "who-we-are.html")