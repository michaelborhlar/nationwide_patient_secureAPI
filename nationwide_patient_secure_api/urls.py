from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, HospitalViewSet, LGAViewSet, StateViewSet, MedicalRecordViewSet, CustomUserViewSet, VitalsViewSet, AccessLogViewSet, LoginView, RegisterView


router = DefaultRouter()
router.register(r'Patient', PatientViewSet)
router.register(r'Hospital', HospitalViewSet)
router.register(r'LGA', LGAViewSet)
router.register(r'State', StateViewSet)
router.register(r'MedicalRecord', MedicalRecordViewSet)
router.register(r'User', CustomUserViewSet)
router.register(r'AccessLog', AccessLogViewSet)
router.register(r'Vitals', VitalsViewSet)

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/register', RegisterView.as_view(), name='register'),
    path('api/auth/login', LoginView.as_view(), name='login'),
]
