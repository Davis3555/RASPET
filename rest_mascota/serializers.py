from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from core.models import registroMascotas, apoderado

class mascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = registroMascotas
        fields = '__all__'
        
class apoderadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = apoderado
        fields = '__all__'