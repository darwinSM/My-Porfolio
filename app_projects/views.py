from django.shortcuts import render
from app_projects.models import Project
from django.shortcuts import get_object_or_404

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