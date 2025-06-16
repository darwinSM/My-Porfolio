from django.db import models
from django.contrib.auth.models import User

class Technology(models.Model):
    CATEGORY_CHOICES = [
    ("language", "Language"),
    ("framework", "Framework"),
    ("database", "Database"),
    ("tool", "Tool"),
    ("platform", "Platform"),
    ("frontend", "Frontend"),
    ("backend", "Backend"),
    ("other", "Other"),
]
        
    title = models.CharField(max_length=50, blank=False, null=True, unique=True)
    icon = models.CharField(max_length=100, blank=True, null=True) # Ej: "fa-brands fa-python" usando FontAwesome
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="other")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.category}"
    
    
    class Meta:
        verbose_name_plural = "technologies"

class AboutMe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    bio = models.TextField()
    nationallity = models.CharField(max_length=50, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="aboutme/picture/", blank=True, null=True)
    cv_pdf = models.FileField(upload_to="aboutme/cv/", blank=True, null=True)
    #cv_pdf = CloudinaryField('CV PDF', resource_type='raw', folder='aboutme/cv/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    technologies = models.ManyToManyField(Technology, blank=True, related_name="profiles")

