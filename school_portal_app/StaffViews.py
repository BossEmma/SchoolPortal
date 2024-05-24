from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import StaffProfile, Gallery, Announcement, Events 




"""def staff_login(request):
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
    return render(request, "login.html")"""



#@login_required(login_url='/accounts/login/')
def bursary_dashboard(request):
    #user = request.user
    return render(request, "student/dashboard.html")




#@login_required(login_url='/accounts/login/')
def staff_dashboard(request):
    #user = request.user
    return render(request, "student/dashboard.html")













