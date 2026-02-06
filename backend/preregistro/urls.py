from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PersonaParticularViewSet,
    EmpresaViewSet,
    PreregistroAPIView,
    ValidarDatosAPIView
)

# Router para ViewSets
router = DefaultRouter()
router.register(r'personas', PersonaParticularViewSet, basename='persona')
router.register(r'empresas', EmpresaViewSet, basename='empresa')

urlpatterns = [
    # Rutas del router
    path('', include(router.urls)),
    
    # Endpoint unificado para crear preregistro
    path('preregistro/', PreregistroAPIView.as_view(), name='preregistro-crear'),
    
    # Endpoint para validar datos
    path('validar/', ValidarDatosAPIView.as_view(), name='validar-datos'),
]
