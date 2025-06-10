from django.db import models
from django.contrib.auth.models import User
from app_about_me.models import Technology

# Create your models here.
class Project (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="")
    description = models.TextField()
    project_technologies = models.ManyToManyField(Technology, blank=True, related_name="projects")
    project_image = models.ImageField(upload_to="project/project_image/", blank=True, null=True)
    demo_url = models.URLField(blank=True, null=True)
    source_code_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
    
    def display_technologies(self):
        return  ", ".join(tech.title for tech in self.project_technologies.all())
    
    # Relaciones
    # project.project_technologies.all()  # rel. directa (desde Project)
    # technology.project_set.all(), ó technology.projects.all() si hay un related_name  # rel. inversa (desde Technology)