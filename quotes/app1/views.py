from django.shortcuts import render,redirect
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
from . tokens import generate_token
from userhome.models import UserInfo
# def index(request):
#     return render(request, 'app1/index.html')

# def contactUs(request):
#     return render(request, 'app1/contactus.html')

# def aboutUs(request):
#     return render(request, 'app1/aboutus.html')

# def userHome(request):
#     return render(request, 'app1/userhome.html')


# def profile(request):
     
#     return render(request, 'app1/profile.html')


# Create your views here.
# def home(request):
#     return render(request, "authentication/index.html")

def landingpage(request):
    return render(request,"app1/authentication/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']



        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('/')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('/')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('/')
        
       
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('/')
        
        myuser = User.objects.create_user(username, email, pass1)
        # myuser.is_active = False
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        
        # Welcome Email
        subject = "Welcome to GFG- Django Login!!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to Quoter!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nKushal Baral"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email for - Quotes login!!"
        message2 = render_to_string('email_confirmation.html',{
            
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
        )
        email.fail_silently = True
        email.send()
       
        return redirect('/',myuser)
        
        
    return render(request, "app1/authentication/index.html")


def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect("/")
    else:
        return render(request,'activation_failed.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        
        user = authenticate(username=username, password=pass1)
        print(username,pass1)
        print(user)

       
        if user is not None:
            login(request, user)
            user_info, created = UserInfo.objects.get_or_create(user=user)

            # UserInfo.objects.create(user=user)
            # params={"userinfo":user}
            # print(params)
            # params = {"userinfo": user.__dict__}
            # print(params)
            
            
            params = {
            "username": user.username,
            "fname": user.first_name,
            "lname": user.last_name,
            "email": user.email,
            "id":user.id,
            
            }
            messages.success(request, "Logged In Sucessfully!!")

            # return render(request, "userhome/userhome.html",{'params': params})
            # return redirect('userhome:mainpage', user_id=user.id, username=user.username, email=user.email, first_name=user.first_name, last_name=user.last_name)
            return redirect('userhome:mainpage', user_id=user.id,content="all")
            # return redirect('userHome')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('/')
    
    return render(request, "app1/authentication/index.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('/')

