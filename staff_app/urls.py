from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login/', views.staff_login, name="staff_login"),
    path('dashboard/', views.dashboard, name="staff_dashboard"),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)