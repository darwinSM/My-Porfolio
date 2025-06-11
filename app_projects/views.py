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
        call_command('loaddata', 'fixtures/back_up_about_me.json')
        call_command('loaddata', 'fixtures/back_up_projects.json')
        call_command('loaddata', 'fixtures/back_up_technology.json')

        return HttpResponse("Fixtures loaded successfully")
    except Exception as e:
        return HttpResponse(f'Error loading fixtures: {e}')