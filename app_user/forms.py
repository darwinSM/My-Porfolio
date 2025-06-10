from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(
        label="Username",
        min_length=4,
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control mb-3",
            "id": "username"
        })
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "form-control mb-3",
            "placeholder": "example@mail.com",
            "id": "email"
        })
    )

    password = forms.CharField(
        label= "Password",
        min_length=4,
        max_length=20,
        required= True,
        widget= forms.PasswordInput(attrs={
            "class": "form-control mb-3",
            "id": "password",
        })
    )

    password_confirm = forms.CharField(
        label= "Confirm to password",
        min_length=4,
        max_length=20,
        required= True,
        widget= forms.PasswordInput(attrs={
            "class": "form-control mb-3",
            "id": "password_confirm"
        })
    )


    # Validacion de usuario duplicado
    def clean_username(self):
        username = self.cleaned_data.get("username")

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        
        return username
    
    # validacion de email duplicado
    def clean_email (self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        
        return email
    

    # Validacion de password_confirmation no es igual a password 
    def clean(self):
        cleaned_data = super().clean()

        # El metodo clean No requiere self
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password_confirm != password:
            self.add_error("password_confirm", "Passwords do not match")
        
        return cleaned_data