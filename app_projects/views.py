from django.shortcuts import render
from app_projects.models import Project
from django.shortcuts import get_object_or_404

#Temporal
from django.core.management import call_command
from django.http import HttpResponse

# Create your views here
def projects_view (request):
    projects = Project.objects.all().order_by("-created_at")
    return render (request, 'app_projects/projects.html' , {
        "projects": projects
    })

def project_detail(request, pk):
    project = get_object_or_404(Project, id=pk)
    return render (request, "app_projects/project_detail.html", {
        "project": project
    })


#TEMPORAL
def temporal_load_fixtures_view(request):
    try:
        call_command('loaddata', 'fixtures/user.json')
        call_command('loaddata', 'fixtures/back_up_technology.json')
        call_command('loaddata', 'fixtures/back_up_about_me.json')
        call_command('loaddata', 'fixtures/back_up_projects.json')
        
        return HttpResponse("Fixtures loaded successfully")
    except Exception as e:
        return HttpResponse(f'Error loading fixtures: {e}')
    

# En app_about_me/views.py (o donde prefieras para probar)
import cloudinary.uploader
from django.http import HttpResponse # Importa HttpResponse

# Asegúrate de que esta URL o vista SOLO se ejecute para esta prueba
# y la quitas después para evitar subidas constantes o problemas de seguridad.

def test_cloudinary_upload(request):
    if request.method == 'GET':
        try:
            # Intenta subir un archivo muy pequeño de texto como prueba
            # Esto es solo para verificar la conexión
            # El contenido 'Test content' será subido como un archivo de texto.
            # 'test_file_upload' será el ID público del archivo en Cloudinary.
            result = cloudinary.uploader.upload(
                "data:text/plain;base64,VGhpcyBpcyBhIHRlc3QgZmlsZS4=", # Esto es "This is a test file." en base64
                public_id="cloudinary_connection_test",
                resource_type="raw" # Para un archivo de texto simple
            )
            print(f"Cloudinary upload successful: {result.get('url')}")
            return HttpResponse(f"Cloudinary upload successful! Check your Cloudinary Media Library for 'cloudinary_connection_test'. URL: {result.get('url')}")
        except Exception as e:
            print(f"Cloudinary upload failed: {e}")
            return HttpResponse(f"Cloudinary upload failed! Error: {e}", status=500)
    return HttpResponse("Send a GET request to test Cloudinary upload.")