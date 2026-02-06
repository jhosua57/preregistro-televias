from django.db import models
from django.core.validators import EmailValidator, RegexValidator


class BasePreregistro(models.Model):
    """Modelo base abstracto para preregistros"""
    
    METODO_PAGO_CHOICES = [
        ('prepago', 'Prepago'),
        ('postpago', 'Postpago'),
    ]
    
    metodo_pago = models.CharField(max_length=10, choices=METODO_PAGO_CHOICES)
    correo_electronico = models.EmailField(validators=[EmailValidator()])
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(
        max_length=20,
        validators=[RegexValidator(regex=r'^\+?1?\d{7,15}$', message="Número de teléfono inválido")]
    )
    fecha_registro = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    confirmado = models.BooleanField(default=False)
    
    class Meta:
        abstract = True


class PersonaParticular(BasePreregistro):
    """Modelo para preregistro de personas particulares"""
    
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    carnet_identidad = models.CharField(
        max_length=20,
        unique=True,
        validators=[RegexValidator(
            regex=r'^[A-Z0-9\-]+$',
            message="El carnet de identidad solo puede contener letras mayúsculas, números y guiones"
        )]
    )
    celular = models.CharField(
        max_length=20,
        validators=[RegexValidator(regex=r'^\+?1?\d{7,15}$', message="Número de celular inválido")]
    )
    
    class Meta:
        db_table = 'persona_particular'
        verbose_name = 'Persona Particular'
        verbose_name_plural = 'Personas Particulares'
        
    def __str__(self):
        return f"{self.nombres} {self.apellido_paterno} {self.apellido_materno}"
    
    def nombre_completo(self):
        return f"{self.nombres} {self.apellido_paterno} {self.apellido_materno}"


class Empresa(BasePreregistro):
    """Modelo para preregistro de empresas"""
    
    TIPO_EMPRESA_CHOICES = [
        ('publica', 'Pública'),
        ('privada', 'Privada'),
    ]
    
    tipo_empresa = models.CharField(max_length=10, choices=TIPO_EMPRESA_CHOICES)
    nombre_empresa = models.CharField(max_length=200)
    responsable = models.CharField(max_length=200)
    nit = models.CharField(
        max_length=20,
        unique=True,
        validators=[RegexValidator(
            regex=r'^[0-9\-]+$',
            message="El NIT solo puede contener números y guiones"
        )]
    )
    celular = models.CharField(
        max_length=20,
        validators=[RegexValidator(regex=r'^\+?1?\d{7,15}$', message="Número de celular inválido")]
    )
    
    class Meta:
        db_table = 'empresa'
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        
    def __str__(self):
        return self.nombre_empresa
