from django.contrib import admin
from django.urls import include, path
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    
    # path('',views.index,name='index'),
    path('',views.landingpage,name='landingpage'),
    path('accounts/login/',views.landingpage,name='landingpage'),
    # path('contactUs',views.contactUs,name='contactus'),
    # path('aboutUs',views.aboutUs,name='aboutus'),
    # path('userHome',views.userHome,name='userHome'),
    # path('profile',views.profile,name='profile'),

    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signout', views.signout, name='signout'),
    path('userhome/', include('userhome.urls'),name='userhome'),
    
    


]



