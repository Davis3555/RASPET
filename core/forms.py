from dataclasses import fields
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import registroMascotas, apoderado

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]

class mascotaForm(ModelForm):
    class Meta:
        model = registroMascotas
        fields = '__all__'

class apoderadoForm(ModelForm): 
    class Meta:
        model = apoderado
        fields = '__all__'
        