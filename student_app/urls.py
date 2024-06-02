from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login/', views.student_login, name="student_login"),
    path('dashboard/', views.dashboard, name="student_dashboard"),
    path('results/', views.results, name="student_results"),
    path('announcements/', views.announcements, name="student_announcements"),
    path('make_payment/', views.make_payment, name="student_make_payment"),
    path('update_payment/', views.update_payment, name="student_update_payment"),
    path('payment_guideline/', views.payment_guideline, name="student_payment_guideline"),
    path('transaction_history/', views.transaction_history, name="student_transaction_history"),
    path('fee_structure/', views.fee_structure, name="student_fee_structure"),
    path('profile/', views.student_profile, name="student_profile"),
    path('change_password/', views.change_password, name="student_change_password"),

    path('sign_out/', views.sign_out, name="sign_out"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)