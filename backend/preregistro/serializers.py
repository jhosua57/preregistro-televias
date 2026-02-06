from rest_framework import serializers
from .models import PersonaParticular, Empresa


class PersonaParticularSerializer(serializers.ModelSerializer):
    """Serializer para Persona Particular con validaciones"""
    
    class Meta:
        model = PersonaParticular
        fields = [
            'id',
            'nombres',
            'apellido_paterno',
            'apellido_materno',
            'direccion',
            'carnet_identidad',
            'telefono',
            'celular',
            'correo_electronico',
            'metodo_pago',
            'confirmado',
            'fecha_registro',
        ]
        read_only_fields = ['id', 'fecha_registro']
    
    def validate_nombres(self, value):
        """Validar que nombres no esté vacío y tenga formato correcto"""
        if not value or not value.strip():
            raise serializers.ValidationError("El campo nombres es requerido")
        if len(value.strip()) < 2:
            raise serializers.ValidationError("El nombre debe tener al menos 2 caracteres")
        return value.strip()
    
    def validate_apellido_paterno(self, value):
        """Validar apellido paterno"""
        if not value or not value.strip():
            raise serializers.ValidationError("El apellido paterno es requerido")
        if len(value.strip()) < 2:
            raise serializers.ValidationError("El apellido debe tener al menos 2 caracteres")
        return value.strip()
    
    def validate_apellido_materno(self, value):
        """Validar apellido materno"""
        if not value or not value.strip():
            raise serializers.ValidationError("El apellido materno es requerido")
        if len(value.strip()) < 2:
            raise serializers.ValidationError("El apellido debe tener al menos 2 caracteres")
        return value.strip()
    
    def validate_carnet_identidad(self, value):
        """Validar formato del carnet de identidad"""
        if not value or not value.strip():
            raise serializers.ValidationError("El carnet de identidad es requerido")
        value = value.strip().upper()
        if len(value) < 5:
            raise serializers.ValidationError("El carnet debe tener al menos 5 caracteres")
        return value


class EmpresaSerializer(serializers.ModelSerializer):
    """Serializer para Empresa con validaciones"""
    
    class Meta:
        model = Empresa
        fields = [
            'id',
            'tipo_empresa',
            'nombre_empresa',
            'responsable',
            'nit',
            'correo_electronico',
            'direccion',
            'telefono',
            'celular',
            'metodo_pago',
            'confirmado',
            'fecha_registro',
        ]
        read_only_fields = ['id', 'fecha_registro']
    
    def validate_nombre_empresa(self, value):
        """Validar nombre de empresa"""
        if not value or not value.strip():
            raise serializers.ValidationError("El nombre de la empresa es requerido")
        if len(value.strip()) < 3:
            raise serializers.ValidationError("El nombre debe tener al menos 3 caracteres")
        return value.strip()
    
    def validate_responsable(self, value):
        """Validar nombre del responsable"""
        if not value or not value.strip():
            raise serializers.ValidationError("El nombre del responsable es requerido")
        if len(value.strip()) < 3:
            raise serializers.ValidationError("El nombre debe tener al menos 3 caracteres")
        return value.strip()
    
    def validate_nit(self, value):
        """Validar formato del NIT"""
        if not value or not value.strip():
            raise serializers.ValidationError("El NIT es requerido")
        value = value.strip()
        if len(value) < 5:
            raise serializers.ValidationError("El NIT debe tener al menos 5 caracteres")
        return value


class PreregistroResumenSerializer(serializers.Serializer):
    """Serializer para el resumen del preregistro"""
    tipo_registro = serializers.ChoiceField(choices=['persona', 'empresa'])
    datos = serializers.DictField()
    
    def validate(self, data):
        """Validar que los datos sean correctos según el tipo de registro"""
        tipo = data.get('tipo_registro')
        datos = data.get('datos')
        
        if tipo == 'persona':
            serializer = PersonaParticularSerializer(data=datos)
        elif tipo == 'empresa':
            serializer = EmpresaSerializer(data=datos)
        else:
            raise serializers.ValidationError("Tipo de registro inválido")
        
        if not serializer.is_valid():
            raise serializers.ValidationError({
                'errores_validacion': serializer.errors
            })
        
        return data
