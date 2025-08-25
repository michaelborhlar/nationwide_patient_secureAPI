from rest_framework import serializers
from .models import Patient, State, LGA, MedicalRecord, AccessLog, User, Hospital, Vitals


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class StateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = State
        fields = "__all__"

class LGASerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LGA
        fields = "__all__"

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Patient
        fields = "__all__"


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = "__all__"

class VitalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vitals
        fields = "__all__"

class AccessLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessLog
        fields = "__all__"




