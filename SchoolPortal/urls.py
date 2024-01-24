"""
URL configuration for SchoolPortal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from school_portal_app import views as school_views
from student_app import views as student_views
from staff_app import views as staff_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # URLs from school_portal_app
    path('', school_views.home, name="home"),
    path('about/', school_views.about, name="about"),
    path('contact/', school_views.contact, name="contact"),

    # URLs from student_app
    path('accounts/student_login', student_views.student_login, name="student_login"),
    path('student/dashboard', student_views.student_dashboard, name="student_dashboard"),

    # URLs from staff_app
    path('accounts/staff_login', staff_views.staff_login, name="staff_login"),
    path('staff/dashboard', staff_views.staff_dashboard, name="staff_dashboard"),

    # URLs from bursary_app
    path('accounts/bursary_login', staff_views.staff_login, name="staff_login"),
    path('busary/dashboard', staff_views.staff_dashboard, name="staff_dashboard"),

    # URLs from ict_app
    path('accounts/ict_login', staff_views.staff_login, name="staff_login"),
    path('ict/dashboard', staff_views.staff_dashboard, name="staff_dashboard"),

    # URLs from principal_app
    path('accounts/principal_login', staff_views.staff_login, name="staff_login"),
    path('principal/dashboard', staff_views.staff_dashboard, name="staff_dashboard"),

]

handler404 = 'school_portal.views.handler404'