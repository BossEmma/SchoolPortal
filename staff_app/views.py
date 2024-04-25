from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponseRedirect, redirect 
from school_portal_app.models import school_name, school_slogan
#from .models import Staff

# Create your views here.

def handler404(request, exception):
    return HttpResponseRedirect('')

def staff_login(request):
    return render(request, "login.html")

#@login_required(login_url='/accounts/staff_login')
def staff_dashboard(request):
    return render(request, "dashboard.html")