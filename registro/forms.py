from django import forms
from django.contrib.auth.forms import UserCreationForm
from modelo.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'nombres', 'apellidos', 'correo', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','placeholder': 'Ingrese su nombre de usuario'}),
            'nombres': forms.TextInput(attrs={'class':'form-control','placeholder': 'Ingrese su nombre'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control','placeholder': 'Ingrese su apellido'}),
            'correo': forms.EmailInput(attrs={'class':'form-control','placeholder': 'Ingrese su correo'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Ingrese su contraseña'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Repita su contraseña'}),

        }

