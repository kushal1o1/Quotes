from django.contrib import admin
from django.urls import path
from .import views
from .views import submit_video
app_name = 'userhome'
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',views.userHome,name='userHome'),
    # path('userhome',views.userHome,name='userHome'),


    path('mainpage/<int:user_id>/contactUs',views.contactUs,name='contactus'),
    path('mainpage/<int:user_id>/aboutUs',views.aboutUs,name='aboutus'),
   
    path('mainpage/<int:user_id>/profile',views.profile,name='profile'),
    # path('signout', views.signout, name='signout'),
    path('mainpage/<int:user_id>/', views.userHome, name='mainpage'),
    path('mainpage/<int:user_id>/submit_video/', views.submit_video, name='submit_video'),

    
]



