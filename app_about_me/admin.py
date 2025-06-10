from django.contrib import admin
from app_about_me.models import Technology, AboutMe

# Register your models here.
@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    fields = ["title", "icon", "category", "description", "created_at", "updated_at"]
    list_display = ["title", "category", "description", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ["user", "full_name", "display_technologies", "nationallity", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]
    filter_horizontal = ["technologies"]  # Esto activa el widget horizontal para ManyToMany
    search_fields = ["user__username", "technologies"]
    list_filter = ["technologies"]

    def display_technologies(self, obj):
        return ", ".join([tech.title for tech in obj.technologies.all()])
    display_technologies.short_description = "Technologies"


