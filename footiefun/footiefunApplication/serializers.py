from rest_framework import serializers
from .models import Stade

class StadeSerializer(serializers.ModelSerializer):
    class Meta : 
        model=Stade
        fields='__all__'