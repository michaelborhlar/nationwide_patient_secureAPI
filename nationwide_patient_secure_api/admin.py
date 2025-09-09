from django.contrib import admin
from . import models
from .models import State, LGA, Hospital, CustomUser, Patient, Vitals, AccessLog, MedicalRecord


models_to_register = [
    models.State,
    models.LGA,
    models.Hospital,
    models.CustomUser,
    models.Patient,
    models.Vitals,
    models.AccessLog,
    models.MedicalRecord
]

for model in models_to_register:
    admin.site.register(model)
# Register your models here.