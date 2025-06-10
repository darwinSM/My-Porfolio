from django.contrib import admin
from app_projects.models import Project

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "display_technologies", "created_at", "updated_at")
    search_fields = ("title", "description")
    list_filter = ("created_at", "user")
    readonly_fields = ("created_at", "updated_at")
    filter_horizontal = ("project_technologies",)
