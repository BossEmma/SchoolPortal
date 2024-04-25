from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about-us/', views.about, name="about"),
    path('academic_info/', views.academic_info, name="academic_info"),
    path('admission-notice/', views.admission_notice, name="admission_notice"),
    path('staff-and-members/', views.staffs, name="staffs"),
    path('resources-and-facilities/', views.resources, name="resources"),
    path('objectives/', views.objective, name="objective"),
    path('vision-mission-objectives/', views.vision, name="vision"),
    path('news/', views.news, name="news"),
    path('message/', views.message, name="message"),
    path('history/', views.history, name="history"),
    path('gallery/', views.gallery, name="gallery"),
    path('events/', views.event, name="event"),
    path('event-details/', views.event_details, name="event_details"),
    path('blog/', views.blog, name="blog"),
    path('blog_details/', views.blog_details, name="blog_details"),
    path('contact/', views.contact, name="contact"),
]

handler404 = 'school_portal_app.views.handler404'