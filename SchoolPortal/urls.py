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
from school_portal_app import SchoolViews
from school_portal_app import StudentViews
from school_portal_app import StaffViews
from school_portal_app import AdminViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', SchoolViews.home, name="home"),
    path('about-us/', SchoolViews.about, name="about"),
    path('academic_info/', SchoolViews.academic_info, name="academic_info"),
    path('admission-notice/', SchoolViews.admission_notice, name="admission_notice"),
    path('staff-and-members/', SchoolViews.staffs, name="staffs"),
    path('resources-and-facilities/', SchoolViews.resources, name="resources"),
    path('objectives/', SchoolViews.objective, name="objective"),
    path('vision-mission-objectives/', SchoolViews.vision, name="vision"),
    path('message/', SchoolViews.message, name="message"),
    path('history/', SchoolViews.history, name="history"),
    path('gallery/', SchoolViews.gallery, name="gallery"),
    path('events/', SchoolViews.event, name="event"),
    path('event-details/', SchoolViews.event_details, name="event_details"),
    path('blog/', SchoolViews.blog, name="blog"),
    path('blog_details/', SchoolViews.blog_details, name="blog_details"),
    path('contact/', SchoolViews.contact, name="contact"),


    path('student/login', StudentViews.student_login, name="student_login"),
    path('student/dashboard', StudentViews.dashboard, name="student_dashboard"),
    path('student/results', StudentViews.results, name="student_results"),
    path('student/announcements', StudentViews.announcements, name="student_announcements"),
    path('student/make_payment/', StudentViews.make_payment, name="student_make_payment"),
    path('student/update_payment/', StudentViews.update_payment, name="student_update_payment"),
    path('student/payment_guideline/', StudentViews.payment_guideline, name="student_payment_guideline"),
    path('student/transaction_history/', StudentViews.transaction_history, name="student_transaction_history"),
    path('student/fee_structure/', StudentViews.fee_structure, name="student_fee_structure"),
    path('student/profile/', StudentViews.student_profile, name="student_profile"),
    path('student/change_password/', StudentViews.change_password, name="student_change_password"),



    path('staff/dashboard', StaffViews.staff_dashboard, name="staff_dashboard"),




    path('bursary/dashboard', StaffViews.bursary_dashboard, name="bursary_dashboard"),



    path('sign_out/', SchoolViews.sign_out, name="sign_out"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'school_portal_app.SchoolViews.handler404'