from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect


from .models import Staff



dashboard_url = "Dashboard"
results_url = "Results"
E_Payment_url= "E-Payment"
Profile_url= "Profile"
change_pasaaword_url= "Change Password"




def staff_login(request):
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
    return render(request, "staff_login.html")





#@login_required(login_url='staff_login')
def dashboard(request):
    #user= request.user
    #student_data= Student.objects.filter(user=request.user)
    url= "Dashboard"

    return render(request, "staff_dashboard.html")