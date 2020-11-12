from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'TopHotel/index.html')

def about(request):
    return render(request, 'TopHotel/about.html')

def contact(request):
    return render(request, 'TopHotel/contact.html')

def services(request):
    return render(request, 'TopHotel/services.html')