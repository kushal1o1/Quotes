from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.index,name='index'),
    path('contactUs',views.contactUs,name='contactus'),
    path('aboutUs',views.aboutUs,name='aboutus'),
    path('userHome',views.userHome,name='userHome'),





]