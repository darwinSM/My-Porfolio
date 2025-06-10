from django.contrib import admin
from app_contact.models import ContactMessage

# Register your models here.
class ContactMessageAdmin (admin.ModelAdmin):
    fields = ["user", "name" , "email" , "message" , "created_at", "updated_at"]
    list_display = ["user", "name" , "email" , "message" , "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]

admin.site.register(ContactMessage, ContactMessageAdmin)
