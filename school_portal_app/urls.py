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
from school_portal_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('about-us/', views.about, name="about"),
    path('academic_info/', views.academic_info, name="academic_info"),
    path('admission-notice/', views.admission_notice, name="admission_notice"),
    path('staff-and-members/', views.staffs, name="staffs"),
    path('resources-and-facilities/', views.resources, name="resources"),
    path('objectives/', views.objective, name="objective"),
    path('vision-mission-objectives/', views.vision, name="vision"),
    path('message/', views.message, name="message"),
    path('history/', views.history, name="history"),
    path('gallery/', views.gallery, name="gallery"),
    path('events/', views.event, name="event"),
    path('event-details/', views.event_details, name="event_details"),
    path('blog/', views.blog, name="blog"),
    path('blog_details/', views.blog_details, name="blog_details"),
    path('contact/', views.contact, name="contact"),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#handler404 = 'school_portal_app.SchoolViews.handler404'