from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import transaction

from .models import PersonaParticular, Empresa
from .serializers import (
    PersonaParticularSerializer,
    EmpresaSerializer,
    PreregistroResumenSerializer
)


class PersonaParticularViewSet(viewsets.ModelViewSet):
    """ViewSet para gestionar preregistros de personas particulares"""
    
    queryset = PersonaParticular.objects.all()
    serializer_class = PersonaParticularSerializer
    
    def create(self, request, *args, **kwargs):
        """Crear un nuevo preregistro de persona particular"""
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({
                'success': True,
                'message': 'Preregistro creado exitosamente',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'success': False,
            'message': 'Error en la validación de datos',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['patch'])
    def confirmar(self, request, pk=None):
        """Confirmar el preregistro"""
        preregistro = self.get_object()
        preregistro.confirmado = True
        preregistro.save()
        
        serializer = self.get_serializer(preregistro)
        return Response({
            'success': True,
            'message': 'Preregistro confirmado exitosamente',
            'data': serializer.data
        })
    
    @action(detail=False, methods=['post'])
    def validar(self, request):
        """Validar datos sin guardar"""
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            return Response({
                'success': True,
                'message': 'Datos válidos',
                'data': serializer.validated_data
            })
        
        return Response({
            'success': False,
            'message': 'Datos inválidos',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class EmpresaViewSet(viewsets.ModelViewSet):
    """ViewSet para gestionar preregistros de empresas"""
    
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    
    def create(self, request, *args, **kwargs):
        """Crear un nuevo preregistro de empresa"""
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({
                'success': True,
                'message': 'Preregistro creado exitosamente',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'success': False,
            'message': 'Error en la validación de datos',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['patch'])
    def confirmar(self, request, pk=None):
        """Confirmar el preregistro"""
        preregistro = self.get_object()
        preregistro.confirmado = True
        preregistro.save()
        
        serializer = self.get_serializer(preregistro)
        return Response({
            'success': True,
            'message': 'Preregistro confirmado exitosamente',
            'data': serializer.data
        })
    
    @action(detail=False, methods=['post'])
    def validar(self, request):
        """Validar datos sin guardar"""
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            return Response({
                'success': True,
                'message': 'Datos válidos',
                'data': serializer.validated_data
            })
        
        return Response({
            'success': False,
            'message': 'Datos inválidos',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class PreregistroAPIView(APIView):
    """Vista unificada para manejar el proceso completo de preregistro"""
    
    @transaction.atomic
    def post(self, request):
        """
        Crear un nuevo preregistro (persona o empresa)
        Espera: { tipo_registro: 'persona'|'empresa', datos: {...} }
        """
        tipo_registro = request.data.get('tipo_registro')
        datos = request.data.get('datos', {})
        
        if not tipo_registro:
            return Response({
                'success': False,
                'message': 'El tipo de registro es requerido'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if tipo_registro == 'persona':
            serializer = PersonaParticularSerializer(data=datos)
        elif tipo_registro == 'empresa':
            serializer = EmpresaSerializer(data=datos)
        else:
            return Response({
                'success': False,
                'message': 'Tipo de registro inválido'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            instance = serializer.save()
            return Response({
                'success': True,
                'message': 'Preregistro creado exitosamente',
                'tipo_registro': tipo_registro,
                'data': serializer.data,
                'id': instance.id
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'success': False,
            'message': 'Error en la validación de datos',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class ValidarDatosAPIView(APIView):
    """Vista para validar datos sin guardarlos"""
    
    def post(self, request):
        """
        Validar datos del formulario
        Espera: { tipo_registro: 'persona'|'empresa', datos: {...} }
        """
        tipo_registro = request.data.get('tipo_registro')
        datos = request.data.get('datos', {})
        
        if not tipo_registro:
            return Response({
                'success': False,
                'message': 'El tipo de registro es requerido'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if tipo_registro == 'persona':
            serializer = PersonaParticularSerializer(data=datos)
        elif tipo_registro == 'empresa':
            serializer = EmpresaSerializer(data=datos)
        else:
            return Response({
                'success': False,
                'message': 'Tipo de registro inválido'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            return Response({
                'success': True,
                'message': 'Datos válidos',
                'data': serializer.validated_data
            })
        
        return Response({
            'success': False,
            'message': 'Datos inválidos',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
