from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'About_us.html')

def notebook(request):
    return render(request, 'Notebook.html')

def landingpage(request):
    return render(request, 'Secondarylogin.html')

