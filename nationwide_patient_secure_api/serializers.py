from rest_framework import serializers
from .models import Patient, State, LGA, MedicalRecord, AccessLog, BaseModel, User, Hospital, Vitals

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Patient
        fields = "__all__"


class StateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = State
        fields = "__all__"

class LGASerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LGA
        fields = "__all__"

