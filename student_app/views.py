from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect,redirect
from school_portal_app.models import school_name, school_slogan
from .models import StudentProfile

# Create your views here.

def handler404(request, exception):
    return HttpResponseRedirect('')

def student_login(request):
    return render(request, "login.html")

#@login_required(login_url='/accounts/student_login')
def student_dashboard(request):
    return render(request, "dashboard.html")

#@login_required(login_url='/accounts/student_login')
def student_profile(request):
    return render(request, "profile.html")

#@login_required(login_url='/accounts/student_login')
def student_results(request):
    return render(request, "results.html")

#@login_required(login_url='/accounts/student_login')
def student_schoolfees(request):
    return render(request, "school_fees.html")