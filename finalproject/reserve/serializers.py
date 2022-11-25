from dataclasses import fields
from .models import * 
from rest_framework import serializers

class DoctorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Doctors
        fields = '__all__'

class ReserveSerializer(serializers.ModelSerializer):
    inf_turn = DoctorSerializer(many=True)

    class Meta:
        model = Reserve
        fields = '__all__'