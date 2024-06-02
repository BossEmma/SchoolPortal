from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect


from .models import Student, Result
from school_portal_app.models import Subject, Class, Term, SchoolSession



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
            return redirect("student_dashboard")         
        else:
            error_message= "Invalid Username or Password"
            return render(request, "login.html", {"error_message":error_message})
    return render(request, "student_login.html")





@login_required(login_url='student_login')
def dashboard(request):
    user= request.user
    student= Student.objects.get(user=request.user)
    result_count = Result.objects.filter(student=student).count()
    subject_count= Class.objects.get(name=student.student_class).subjects.count()
    term= get_object_or_404(Term)
    url= "Dashboard"
    context = {
        'user':user,
        'student': student,
        'url': url,
        'result_count': result_count,
        'subject_count': subject_count,
        'term':term
    }
    return render(request, "dashboard.html", context)




@login_required(login_url='student_login')
def results(request):
    user = request.user
    student= Student.objects.get(user=request.user)
    results= Result.objects.filter(student=student)

    objects_per_page = 20  
    paginator = Paginator(results, objects_per_page)
    page = request.GET.get('page')
    try:
        paginated_objects = paginator.page(page)
 
    except PageNotAnInteger:
        paginated_objects = paginator.page(1)

    except EmptyPage:
        paginated_objects = paginator.page(paginator.num_pages)

    url= "Results"
    context = {
        'url': url,
        'user':user,
        'student': student,
        'paginated_objects': paginated_objects
    }
    return render(request, "results.html", context)




@login_required(login_url='student_login')
def announcements(request):
    user = request.user
    url= "Announcements"
    context = {
        'url': url,
    }
    return render(request, "announcements.html")





@login_required(login_url='student_login')
def make_payment(request):
    user = request.user
    return render(request, "make_payment.html")




@login_required(login_url='student_login')
def update_payment(request):
    user = request.user
    return render(request, "update_payment.html")





@login_required(login_url='student_login')
def payment_guideline(request):
    user = request.user
    return render(request, "payment_guideline.html")




@login_required(login_url='student_login')
def transaction_history(request):
    user = request.user
    return render(request, "transaction_history.html")





@login_required(login_url='student_login')
def fee_structure(request):
    user = request.user
    return render(request, "fee_structure.html")





@login_required(login_url='student_login')
def student_profile(request):
    user = request.user
    return render(request, "profile.html")





@login_required(login_url='student_login')
def change_password(request):
    user = request.user
    return render(request, "change_password.html")


#@login_required(login_url='/accounts/login/')
def sign_out(request):
    logout(request)
    return redirect("home")