from django.shortcuts import render, redirect
from django.contrib.auth import login, logout   
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.core.exceptions import SuspiciousOperation
import logging
from django.contrib.auth.decorators import login_required
from app_user.forms import RegisterForm
from app_sendmails.mails import send_mail_to_user, send_email_to_admin
from django.utils import timezone


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("app_user")


# Create your views here.
def login_view (request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        # username = request.POST["username"]
        password = request.POST.get("password", "")
        # password = request.POST["password"]

        try:
            user = authenticate(username=username, password=password)

        except SuspiciousOperation as e:
            logger.error(f"Error SuspiciousOperation: {str(e)}")
            messages.error(request, "Login attempt failed due to suspicious activity. Please try again.")
            return redirect("login")

        if user and user.is_active:
                login(request, user)
                messages.success(request, "User login successfully")
                return redirect ("home")
        else:
            messages.error(request, "invalid credencial")
            return redirect("login")
    
    return render (request, 'app_user/login.html', {})


@login_required(login_url="home")
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logout Successfully")
    else:
         messages.warning("No user is logged in")

    return redirect ('home')
     

def register_view(request):

    if request.user.is_authenticated:
        return redirect ("home")

    form = RegisterForm(request.POST or None)

    if request.method == "POST":
             
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            if user:
                login(request, user)

                # Info para envio de correo al usuario
                contex_user = {
                    "name":  user.get_full_name() or user.username,
                    "current_year": timezone.now().year,
                }

                send_mail_to_user(
                    subject=f"Welcome {user.username}. Your account has been created",
                    template_name="app_user/user_registration_confirmation.html",
                    context=contex_user,
                    user_email=user.email
                )

                # Info para envio de correo al admin
                context_admin = {
                    "name": user.get_full_name() or user.username,
                    "email": user.email,
                    "current_year": timezone.now().year,
                    "message": f"New user registered: {user.username}",
                }
                
                send_email_to_admin(
                    subject=f"New user registered: {user.username}",
                    template_name="app_user/admin_new_user_notification.html",
                    context=context_admin,
                    reply_to_email=user.email
                )

                messages.success(request, "user create succesfully")
                return redirect ("home")

        else:
            messages.error(request, "Registration error. Check the fields.")    

    return render (request, "app_user/register.html" , {
         "form": form,
    }) 
             


#! Vistas temporales para crear supeuser desde render
from django.contrib.auth import get_user_model
from django.http import HttpResponse

def temporal_create_superuser_render_view(request):
    User = get_user_model()
    if not User.objects.filter(username="sami").exists():
        User.objects.create_superuser(
            username="sami",
            email="dasarmi01@gmail.com",
            password="1234"
                    )
        return HttpResponse("Superuser create successfully")
    else:
        return HttpResponse("Superuser already exixst")
     
        
def promote_existing_user_to_superuser(request):
    User = get_user_model()
    try:
        user = User.objects.get(username='sami')
        user.is_staff = True
        user.is_superuser = True
        user.set_password('1234')  # Asegura que la contraseña sea válida
        user.save()
        return HttpResponse("User promoted to superuser and password reset.")
    except User.DoesNotExist:
        return HttpResponse("User does not exist.")
    

from django.http import JsonResponse
from django.conf import settings

def test_env(request):
    data = {
        "ENVIRONMENT": getattr(settings, "ENVIRONMENT", "No definido"),
        "DEFAULT_FILE_STORAGE": getattr(settings, "DEFAULT_FILE_STORAGE", "No definido"),
        "CLOUDINARY_URL": getattr(settings, "CLOUDINARY_URL", "No definido"),
    }
    return JsonResponse(data)