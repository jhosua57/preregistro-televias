from django.contrib import admin
from .models import PersonaParticular, Empresa


@admin.register(PersonaParticular)
class PersonaParticularAdmin(admin.ModelAdmin):
    list_display = [
        'nombres',
        'apellido_paterno',
        'apellido_materno',
        'carnet_identidad',
        'metodo_pago',
        'confirmado',
        'fecha_registro'
    ]
    list_filter = ['metodo_pago', 'confirmado', 'fecha_registro']
    search_fields = [
        'nombres',
        'apellido_paterno',
        'apellido_materno',
        'carnet_identidad',
        'correo_electronico'
    ]
    readonly_fields = ['fecha_registro', 'actualizado']
    
    fieldsets = (
        ('Información Personal', {
            'fields': (
                'nombres',
                'apellido_paterno',
                'apellido_materno',
                'carnet_identidad',
            )
        }),
        ('Información de Contacto', {
            'fields': (
                'correo_electronico',
                'telefono',
                'celular',
                'direccion',
            )
        }),
        ('Información del Registro', {
            'fields': (
                'metodo_pago',
                'confirmado',
                'fecha_registro',
                'actualizado',
            )
        }),
    )


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = [
        'nombre_empresa',
        'tipo_empresa',
        'nit',
        'responsable',
        'metodo_pago',
        'confirmado',
        'fecha_registro'
    ]
    list_filter = ['tipo_empresa', 'metodo_pago', 'confirmado', 'fecha_registro']
    search_fields = [
        'nombre_empresa',
        'nit',
        'responsable',
        'correo_electronico'
    ]
    readonly_fields = ['fecha_registro', 'actualizado']
    
    fieldsets = (
        ('Información de la Empresa', {
            'fields': (
                'tipo_empresa',
                'nombre_empresa',
                'nit',
                'responsable',
            )
        }),
        ('Información de Contacto', {
            'fields': (
                'correo_electronico',
                'telefono',
                'celular',
                'direccion',
            )
        }),
        ('Información del Registro', {
            'fields': (
                'metodo_pago',
                'confirmado',
                'fecha_registro',
                'actualizado',
            )
        }),
    )
