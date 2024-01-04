from django.shortcuts import render
def index(request):
    return render(request, 'app1/index.html')

def contactUs(request):
    return render(request, 'app1/contactus.html')

def aboutUs(request):
    return render(request, 'app1/aboutus.html')

def userHome(request):
    return render(request, 'app1/userhome.html')
