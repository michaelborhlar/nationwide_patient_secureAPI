from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient, Hospital, LGA, State, AccessLog, MedicalRecord, Vitals, User
from .serializers import PatientSerializer, HospitalSerializer, StateSerializer, LGASerializer, AccessLogSerializer, MedicalRecordSerializer, VitalsSerializer, UserSerializer

# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class LGAViewSet(viewsets.ModelViewSet):
    queryset = LGA.objects.all()
    serializer_class = LGASerializer
class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer

class AccessLogViewSet(viewsets.ModelViewSet):
    queryset = AccessLog.objects.all()
    serializer_class = AccessLogSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
 
class VitalsViewSet(viewsets.ModelViewSet):
    queryset = Vitals.objects.all()
    serializer_class = VitalsSerializer



    