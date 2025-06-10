from django.shortcuts import render
from app_about_me.models import  Technology, AboutMe

# Create your views here.
def about_me_view (request):
    profile = AboutMe.objects.first() # Siempre traerá el primer perfil (el tuyo), el sitio cargará sin importar si hay un usuario autenticado o no.
    return render (request, 'app_about_me/about_me.html', {
        "profile": profile,
    })