from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient, Hospital, LGA, State
from .serializers import PatientSerializer, HospitalSerializer, StateSerializer, LGASerializer

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
    