from rest_framework import serializers
from .models import Patient, State, LGA, MedicalRecord, AccessLog, CustomUser, Hospital, Vitals
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ['id','username','email','password']

    def create(self, validated_data):

        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']

        )

        return user

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if not user:
            raise serializers.ValidationError({'error': "invalid login credentials"})
        return user
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
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




