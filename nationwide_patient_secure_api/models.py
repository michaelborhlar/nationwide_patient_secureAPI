from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)  # when created
    updated_at = models.DateTimeField(auto_now=True)      # when last updated

    class Meta:
        abstract = True 


class State(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class LGA(BaseModel):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Hospital(BaseModel):
    name = models.CharField(max_length=50)
    lga =models.ForeignKey(LGA, on_delete=models.CASCADE)
    adress = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users"
    )
    role = models.CharField(
        max_length=20,
        choices=[
            ("NURSE", "Nurse"),
            ("DOCTOR", "Doctor"),
            ("ADMIN", "Admin"),
            ("SUPERADMIN", "SuperAdmin"),
        ],
    )

    def __str__(self):
        return self.username
# create patient model
class Patient(BaseModel):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="patients")
    full_name = models.CharField(max_length=150)
    dob = models.DateField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name

# create models for medical record with foreign key
class MedicalRecord(BaseModel):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name="medical_record")
    diagnoses = models.TextField()
    medications = models.TextField()
    allergies = models.TextField(blank=True, null=True)
    test_results = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name

# create vital model
class Vitals(BaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="vitals")
    recorded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="vitals_taken")
    blood_pressure = models.CharField(max_length=20)
    heart_rate = models.IntegerField()
    temperature = models.FloatField()
    def __str__(self):
        return self.name
# audit/models.py
class AccessLog(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="access_logs")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="access_logs")
    action = models.CharField(max_length=50)  # e.g., VIEWED, UPDATED, DELETED
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

