from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ContactMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="contac_messages")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "ContactMessage"
        verbose_name = "Contacto"

    def __str__(self):
        return f"{self.name} - ({self.email})"

    # Metodo de clase para crear una instancia de ContactMessage
    @classmethod
    def create_contact_message(cls, form_data, user=None):
        message_obj = cls.objects.create(
            user=user if user and user.is_authenticated else None,
            name=form_data.get("name"),
            email=form_data.get("email"),
            message=form_data.get("message"),
            )
        return message_obj
        