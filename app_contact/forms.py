from django import forms
from app_contact.models import ContactMessage

class ContactForm(forms.Form):
    name = forms.CharField(
        label= "Name:",
        min_length=4,
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            "class":"form-control mb-3",
            'id' : "name",
        })
    )

    email = forms.EmailField(
        label="Email:",
        required=True,
        widget=forms.EmailInput(attrs={
            "class":"form-control mb-3",
            "id":"email",
        })
    )

    message = forms.CharField(
        label = "Message:",
        required=True,
        widget=forms.Textarea(attrs={
            "class":"form-control mb-3",
            "id":"message",
            "rows":5,
            "placeholder" : "Write your message here..."
        })
    )


# Esta clase se adiciona, para poder hacer edicion del formulario (solo en el campo message), pues para que el formulario se pueda editar es indispensable que herede de ModelForm (que sea de un modelo), La vista UpdateView requiere un formulario que sepa trabajar con una instancia del modelo (instance=...). Eso solo lo puede hacer un ModelForm.
class ContactMessageUpdateForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["message"]

        widgets = {
            'message': forms.Textarea(attrs={
                "class":"form-control mb-3",
                'id': "message",
                "rows": 5,
                "placeholder": "Write your message here..."
            })
        }
    