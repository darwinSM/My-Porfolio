from django.conf import settings    
from django.template.loader import get_template
import threading
from django.core.mail import EmailMultiAlternatives
from django.urls import reverse

class EmailSender:
        # Inicializa una instancia con parámetros necesarios para el correo
    def __init__ (self, subject , template_name , context , recipient_list, from_mail=None, reply_to=None):

        self.subject = subject
        self.template_name = template_name
        self.context = context
        self.recipient_list = recipient_list
        # Si from_email no se proporciona, utiliza el EMAIL_HOST_USER de las configuraciones
        self.from_email = from_mail or settings.EMAIL_HOST_USER
        self.reply_to = reply_to or []


    def send(self):
        # Obtiene el template utilizando get_template y renderiza con el contexto proporcionado
        template = get_template(self.template_name)
        html_message = template.render(self.context)
        # Crea y arranca un hilo para enviar el correo asincrónicamente
        thread = threading.Thread(
            target=self._send_mail,
            args=(self.subject, self.from_email , self.recipient_list , self.reply_to, html_message)
        )
        thread.start()

    @staticmethod    
    def _send_mail(subject, from_email, recipient_list, reply_to, html_message):
            # Envía el correo utilizando la función send_mail de Django
            message = EmailMultiAlternatives(
                 subject=subject,
                 body="",
                 from_email=from_email,
                 to=recipient_list,
                 reply_to=reply_to
            )

            message.attach_alternative(html_message, "text/html")

            message.send()

# Envia correo al admin
def send_email_to_admin(subject, template_name, context, reply_to_email=None):
    EmailSender(
        subject=subject,
        template_name=template_name,
        context=context,
        recipient_list=["dasarmi01@gmail.com"],
        reply_to=["reply_to_email"] if reply_to_email else []
    ).send()


# Envia correo al usuario
def send_mail_to_user(subject, template_name, context, user_email):
     EmailSender(
          subject=subject,
          template_name=template_name,
          context=context,
          recipient_list=[user_email],
          reply_to=["dasarmi01@gmail.com"]
     ).send()

