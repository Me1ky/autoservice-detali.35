from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def prices(request):
    return render(request, 'main/prices.html')

def contacts(request):
    return render(request, 'main/contacts.html')