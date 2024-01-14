from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from quotes import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes ,force_str
from django.contrib.auth import authenticate, login, logout
from .models import UserInfo
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from .models import Video

# from . tokens import generate_token
# def index(request):
#     return render(request, 'app1/index.html')

def contactUs(request,user_id):
    return render(request, 'userhome/contactus.html')

def aboutUs(request,user_id):
    return render(request, 'userhome/aboutus.html')


# def mainpage(request, user_id, username, email, first_name, last_name):
#     # Your mainpage logic
#     # You can use user_id, username, email, first_name, last_name to personalize the content

#     return render(request, 'userhome/mainpage.html', {'user_id': user_id, 'username': username, 'email': email, 'first_name': first_name, 'last_name': last_name})
@login_required
def userHome(request,user_id):
    user_info = get_object_or_404(UserInfo, user_id=user_id)
    videos = Video.objects.all().order_by('-posted_date')
    if request.method == 'POST':
        print("wrking")
        title = request.POST.get('title')
        description = request.POST.get('description')
        video_file = request.FILES.get('video_file')
        print(title,description)

        if title and description and video_file:
            # Save the video file to your desired location (e.g., MEDIA_ROOT)
            file_path = default_storage.save(f'videos/{video_file.name}', video_file)

            # Create a Video object in the database
            video = Video.objects.create(
                user=user_info.user,
               
                 # If you want to store the username in the Video model
                title=title,
                description=description,
                video_file=file_path,
                # Set additional fields accordingly
            )


   
    return render(request, 'userhome/userhome.html',{'user_info': user_info ,'videos': videos})


@login_required
def profile(request,user_id):

   
    user = get_object_or_404(User, id=user_id)
    user_info = get_object_or_404(UserInfo, user_id=user_id)
    videos = Video.objects.filter(user=user_info.user).order_by('-posted_date')

    if request.method == 'POST':
        # Get data from the POST request
        profile_picture = request.FILES.get('profile_picture')
        bio = request.POST.get('bio')
        website = request.POST.get('website')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Update UserInfo model with the provided data
        if profile_picture:
            user_info.profile_picture = profile_picture
        if bio:
            user_info.bio = bio
        if website:
            user_info.website = website

        # Update User model with the provided data
        if username:
            user.username = username
        if email:
            user.email = email
        if password:
            user.set_password(password)

        user_info.save()
        user.save()
    return render(request, 'userhome/profile.html',{'user': user, 'user_info': user_info ,'videos': videos})


# Create your views here.
# def home(request):
#     return render(request, "authentication/index.html")

def landingpage(request):
    return render(request,"app1/authentication/index.html")

# @login_required
def submit_video(request,user_id):
    print("wrking")
    if request.method == 'POST':
        print("wrking")
        title = request.POST.get('title')
        description = request.POST.get('description')
        video_file = request.FILES.get('video_file')

        if title and description and video_file:
            # Save the video file to your desired location (e.g., MEDIA_ROOT)
            file_path = default_storage.save(f'videos/{video_file.name}', video_file)

            # Create a Video object in the database
            video = Video.objects.create(
                user=request.user,
                username=request.user.username,  # If you want to store the username in the Video model
                title=title,
                description=description,
                video_file=file_path,
                # Set additional fields accordingly
            )

            return redirect('mainpage')  # Redirect to a page showing the list of videos

    return render(request, 'userhome/userhome.html')

