from django.shortcuts import render, redirect, HttpResponseRedirect

# Create your views here.

def handler404(request, exception):
    return HttpResponseRedirect('')

def home(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")