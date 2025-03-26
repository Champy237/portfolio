from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def service(request):
    return render(request,'sevice.html')
def realisation(request):
    return render(request,'realisation.html')
def contact(request):
    return render(request,'contact.html')


