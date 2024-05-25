from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect


from .models import Gallery, Announcement, Events, Student



dashboard_url = "Dashboard"
results_url = "Results"
E_Payment_url= "E-Payment"
Profile_url= "Profile"
change_pasaaword_url= "Change Password"







def student_login(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        user= authenticate(request, email=email, password=password)
    
        if user is not None: 
            login(request, user)
            return redirect("dashboard")         
        else:
            error_message= "Invalid Username or Password"
            return render(request, "login.html", {"error_message":error_message})
    return render(request, "student_login.html")





@login_required(login_url='/student/login/')
def dashboard(request):
    user = request.user.student
    url= "Dashboard"
    context = {
        'user':user,
        'url': url
    }
    return render(request, "student/dashboard.html", context)




@login_required(login_url='/student/login/')
def results(request):
    user = request.user
    url= "Results"
    context = {
        'url': url,
    }
    return render(request, "student/results.html", context)




@login_required(login_url='/student/login/')
def announcements(request):
    user = request.user
    url= "Announcements"
    context = {
        'url': url,
    }
    return render(request, "student/announcements.html")





@login_required(login_url='/student/login/')
def make_payment(request):
    user = request.user
    return render(request, "student/make_payment.html")




@login_required(login_url='/student/login/')
def update_payment(request):
    user = request.user
    return render(request, "student/update_payment.html")





@login_required(login_url='/student/login/')
def payment_guideline(request):
    user = request.user
    return render(request, "student/payment_guideline.html")




@login_required(login_url='/student/login/')
def transaction_history(request):
    user = request.user
    return render(request, "student/transaction_history.html")





@login_required(login_url='/student/login/')
def fee_structure(request):
    user = request.user
    return render(request, "student/fee_structure.html")





@login_required(login_url='/student/login/')
def student_profile(request):
    user = request.user
    return render(request, "student/profile.html")





@login_required(login_url='/student/login/')
def change_password(request):
    user = request.user
    return render(request, "student/change_password.html")
