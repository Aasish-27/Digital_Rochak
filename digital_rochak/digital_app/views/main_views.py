from django.shortcuts import render
# Create your views here.

def home_view(request):
    return render(request,'main/index.html')

def about_view(request):
    return render(request,'main/about.html')

def services_view(request):
    return render(request,'main/services.html')

def contact_view(request):
    return render(request,'main/contact.html')