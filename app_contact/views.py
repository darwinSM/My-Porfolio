from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse_lazy

from app_contact.models import ContactMessage
from app_contact.forms import ContactForm, ContactMessageUpdateForm
from app_sendmails.mails import send_mail_to_user, send_email_to_admin

import logging


logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger("app_contact")

# Create your views here.
def contact_view(request):
    form = ContactForm(request.POST or None)
    user = request.user

    if request.method == "POST" and form.is_valid():
        logger.warning("✅ Entró a contact_view")  # Prueba 1
        print("=== Datos limpios del formulario ===")
        logger.info(f" .... datos del fomulario.... {form.cleaned_data}")

        # Mensaje de le usuario al administrador 
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        message = form.cleaned_data["message"]

        #Guardar info del contacto y mensaje en la base de datos
        ContactMessage.create_contact_message(
                                            form_data=form.cleaned_data, 
                                            user=user)
        
        context_admin = {
            "name":name,
            "email": email,
            "message":message,
            "current_year":timezone.now().year,
        }

        send_email_to_admin(
            subject=f"New contact message from  {name}",
            template_name = "app_contact/send_admin_notification_email.html",
            context=context_admin,
            reply_to_email=email
        )

        # Enviar respuesta automatica del administrador al usuario
        message_response = f"Hello { name }, Thank you for visiting my portfolio. I Have recive you message and will contact you soon"


        context_user={
            "name": name,
            "message": message_response,
            "currebt_year": timezone.now().year,
        }

        send_mail_to_user(
            subject=f"Hello {name}. Thank you for your message",
            template_name="app_contact/send_user_confirmation_email.html",
            context=context_user,
            user_email=email
        )


        messages.success(request, "Message sent successfully")
        return redirect('home')

    linkedin_url = "https://www.linkedin.com/in/darwing-sarmiento-moreno-2b9394259/"
    github_url = "https://github.com/darwinSM"
    
    return render(request, "app_contact/contact.html", {
        'form': form,
        'linkedin_url': linkedin_url,
        'github_url': github_url,
        })




class ContactMessageListView(LoginRequiredMixin, ListView):
    model = ContactMessage
    login_url = "home"
    template_name = "app_contact/contact_message_list.html"
    
    def get_queryset(self):
        user=self.request.user
        get_queryset = ContactMessage.objects.filter(user=user).order_by("-updated_at")
        return get_queryset
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.get_queryset()
        context["messages_updated"] = [message.id for message in context["object_list"] if message.updated_at > message.created_at]
        return context
    

class ContactMessageDetailView(LoginRequiredMixin, DetailView):
    model = ContactMessage
    login_url = 'home'
    template_name = "app_contact/contact_message_detail.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = self.get_object()
        return context
    
    def get_queryset(self):
        return ContactMessage.objects.filter(user=self.request.user)
    
class ContactMessageUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ContactMessage
    login_url = 'home'
    template_name = "app_contact/contact_message_update.html"
    form_class = ContactMessageUpdateForm
    success_message = "contactmessage updated successfully"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_success_url (self):
        return reverse_lazy ('contact_messages_list')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.id != self.get_object().user_id:
            messages.error(request, "You are not authorized to edit this message.")
            return redirect ('home')
        return super().dispatch(request, *args, **kwargs)
    
    
class ContactMessageDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = ContactMessage
    login_url = "home"
    template_name = "app_contact/contact_message_confirm_delete.html"
    success_message = "Message delete successfully"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = self.get_object()
        return context
    
    def get_success_url (self):
        return reverse_lazy ("contact_messages_list")
    
    def dispatch (self, request, *args, **kwargs):
        if request.user.id != self.get_object().user_id:
            messages.error(request, "You are not authorized to delete this message.")
            return redirect ("home")
        return super().dispatch(request, *args, **kwargs)
