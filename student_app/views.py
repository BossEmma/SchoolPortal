#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect#,redirect, 
#from .models import StudentProfile

# Create your views here.

def handler404(request, exception):
    return HttpResponseRedirect('')

def student_login(request):
    return render(request, "login.html")

#@login_required(login_url='/accounts/student_login')
def student_dashboard(request):
    return render(request, "dashboard.html")

def student_profile(request):
    return render(request, "profile.html")

def student_results(request):
    return render(request, "results.html")

def student_schoolfees(request):
    return render(request, "school_fees.html")