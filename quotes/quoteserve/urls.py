from django.contrib import admin
from django.urls import path
from .import views
# from .views import submit_video
app_name = 'userhome'
urlpatterns = [
  
  path("quotes/",views.random_quotes_view,name='random_quotes_view'),
    
]
