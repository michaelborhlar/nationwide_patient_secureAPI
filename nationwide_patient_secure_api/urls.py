from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, HospitalViewSet, LGAViewSet, StateViewSet


router = DefaultRouter()
router.register(r'Patient', PatientViewSet)
router.register(r'Hospital', HospitalViewSet)
router.register(r'LGA', LGAViewSet)
router.register(r'State', StateViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]
