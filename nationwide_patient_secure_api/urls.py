from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, HospitalViewSet, LGAViewSet, StateViewSet, MedicalRecordViewSet, UserViewSet, VitalsViewSet, AccessLogViewSet


router = DefaultRouter()
router.register(r'Patient', PatientViewSet)
router.register(r'Hospital', HospitalViewSet)
router.register(r'LGA', LGAViewSet)
router.register(r'State', StateViewSet)
router.register(r'MedicalRecord', MedicalRecordViewSet)
router.register(r'User', UserViewSet)
router.register(r'AccessLog', AccessLogViewSet)
router.register(r'Vitals', VitalsViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]
