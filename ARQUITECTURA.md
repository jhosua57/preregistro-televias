# Arquitectura del Sistema de Preregistro

## Diagrama de Arquitectura General

```
┌─────────────────────────────────────────────────────────────┐
│                        USUARIO FINAL                        │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        │ HTTP/HTTPS
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                    FRONTEND (Vue 3)                         │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Componentes UI                                      │   │
│  │  - StepIndicator.vue                                 │   │
│  │  - Paso1.vue (Selección)                            │   │
│  │  - Paso2.vue (Captura de Datos)                     │   │
│  │  - Paso3.vue (Confirmación)                         │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Estado Global (Pinia)                               │   │
│  │  - preregistro.js                                    │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Servicios                                           │   │
│  │  - api.js (Axios)                                    │   │
│  └──────────────────────────────────────────────────────┘   │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        │ REST API
                        │ (JSON)
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                 BACKEND (Django REST Framework)             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  API Endpoints (views.py)                            │   │
│  │  - PreregistroAPIView                                │   │
│  │  - ValidarDatosAPIView                               │   │
│  │  - PersonaParticularViewSet                          │   │
│  │  - EmpresaViewSet                                    │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Serializers (serializers.py)                        │   │
│  │  - PersonaParticularSerializer                       │   │
│  │  - EmpresaSerializer                                 │   │
│  │  - Validaciones                                      │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Modelos de Datos (models.py)                        │   │
│  │  - PersonaParticular                                 │   │
│  │  - Empresa                                           │   │
│  │  - BasePreregistro (abstracto)                       │   │
│  └──────────────────────────────────────────────────────┘   │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        │ ORM
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                   BASE DE DATOS (SQLite)                    │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Tablas:                                             │   │
│  │  - persona_particular                                │   │
│  │  - empresa                                           │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## Diagrama de Flujo del Usuario

```
┌─────────────────┐
│  Página Inicio  │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│         PASO 1: SELECCIÓN               │
│                                         │
│  ┌──────────────────┐                  │
│  │ Tipo de Registro │                  │
│  │  ○ Persona       │                  │
│  │  ○ Empresa       │                  │
│  └──────────────────┘                  │
│                                         │
│  ┌──────────────────┐                  │
│  │ Método de Pago   │                  │
│  │  ○ Prepago       │                  │
│  │  ○ Postpago      │                  │
│  └──────────────────┘                  │
└────────┬────────────────────────────────┘
         │
         │ [Siguiente]
         ▼
┌─────────────────────────────────────────┐
│    PASO 2: CAPTURA DE DATOS             │
│                                         │
│  Si Persona:          Si Empresa:       │
│  - Nombres            - Tipo Empresa    │
│  - Apellido Paterno   - Nombre Empresa  │
│  - Apellido Materno   - Responsable     │
│  - CI                 - NIT             │
│  - Teléfono           - Email           │
│  - Celular            - Dirección       │
│  - Email              - Teléfono        │
│  - Dirección          - Celular         │
│                                         │
│  [Validación en tiempo real]            │
└────────┬────────────────────────────────┘
         │
         │ [Siguiente]
         ▼
┌─────────────────────────────────────────┐
│    PASO 3: RESUMEN Y CONFIRMACIÓN       │
│                                         │
│  ┌───────────────────────────────────┐  │
│  │  Resumen de todos los datos       │  │
│  │  ingresados                       │  │
│  └───────────────────────────────────┘  │
│                                         │
│  [Editar] [Confirmar y Enviar]          │
└────────┬────────────────────────────────┘
         │
         │ [Confirmar]
         ▼
┌─────────────────────────────────────────┐
│         ENVÍO AL BACKEND                │
│  POST /api/preregistro/                 │
└────────┬────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│      CONFIRMACIÓN EXITOSA               │
│  ✓ Preregistro completado               │
│  ✓ Email de confirmación enviado        │
└─────────────────────────────────────────┘
```

## Modelo de Datos

```
┌──────────────────────────────────────────────────────┐
│            BasePreregistro (Abstracto)               │
├──────────────────────────────────────────────────────┤
│ + metodo_pago: CharField                             │
│ + correo_electronico: EmailField                     │
│ + direccion: CharField                               │
│ + telefono: CharField                                │
│ + fecha_registro: DateTimeField                      │
│ + actualizado: DateTimeField                         │
│ + confirmado: BooleanField                           │
└──────────────────────────┬───────────────────────────┘
                           │
         ┌─────────────────┴─────────────────┐
         │                                   │
         ▼                                   ▼
┌─────────────────────┐         ┌─────────────────────┐
│  PersonaParticular  │         │      Empresa        │
├─────────────────────┤         ├─────────────────────┤
│ + nombres           │         │ + tipo_empresa      │
│ + apellido_paterno  │         │ + nombre_empresa    │
│ + apellido_materno  │         │ + responsable       │
│ + carnet_identidad  │         │ + nit (unique)      │
│   (unique)          │         │ + celular           │
│ + celular           │         │                     │
│                     │         │                     │
│ Hereda:             │         │ Hereda:             │
│ - metodo_pago       │         │ - metodo_pago       │
│ - correo_electronico│         │ - correo_electronico│
│ - direccion         │         │ - direccion         │
│ - telefono          │         │ - telefono          │
│ - fecha_registro    │         │ - fecha_registro    │
│ - actualizado       │         │ - actualizado       │
│ - confirmado        │         │ - confirmado        │
└─────────────────────┘         └─────────────────────┘
```

## Flujo de Datos

```
1. SELECCIÓN INICIAL (Paso 1)
   ┌──────────────┐
   │   Usuario    │
   └──────┬───────┘
          │ Selecciona tipo y método
          ▼
   ┌──────────────┐
   │  Pinia Store │ ← Almacena selección
   └──────────────┘

2. CAPTURA DE DATOS (Paso 2)
   ┌──────────────┐
   │   Usuario    │ Ingresa datos
   └──────┬───────┘
          │
          ▼
   ┌──────────────┐
   │  Componente  │ Validación en tiempo real
   │   Paso2.vue  │
   └──────┬───────┘
          │
          ▼
   ┌──────────────┐
   │  Pinia Store │ ← Almacena datos
   └──────────────┘

3. CONFIRMACIÓN (Paso 3)
   ┌──────────────┐
   │  Pinia Store │ Obtiene todos los datos
   └──────┬───────┘
          │
          ▼
   ┌──────────────┐
   │   api.js     │ Prepara payload
   └──────┬───────┘
          │
          │ POST /api/preregistro/
          ▼
   ┌──────────────────────┐
   │  Django Backend      │
   │  PreregistroAPIView  │
   └──────┬───────────────┘
          │
          │ Validación
          ▼
   ┌──────────────────────┐
   │    Serializer        │
   │  Validación de datos │
   └──────┬───────────────┘
          │
          │ Si válido
          ▼
   ┌──────────────────────┐
   │    ORM Django        │
   │  Guarda en DB        │
   └──────┬───────────────┘
          │
          ▼
   ┌──────────────────────┐
   │  Base de Datos       │
   │  (SQLite)            │
   └──────────────────────┘
```

## Tecnologías por Capa

### Frontend
```
┌─────────────────────────────────────┐
│  Vue 3 - Framework JavaScript       │
│  Vite - Build Tool                  │
│  Tailwind CSS - Estilos             │
│  PrimeVue - Componentes UI          │
│  Pinia - Gestión de Estado          │
│  Vue Router - Navegación            │
│  Axios - Cliente HTTP               │
└─────────────────────────────────────┘
```

### Backend
```
┌─────────────────────────────────────┐
│  Django 5.0 - Framework Web         │
│  Django REST Framework - API        │
│  django-cors-headers - CORS         │
│  SQLite - Base de Datos             │
└─────────────────────────────────────┘
```

## Patrones de Diseño Utilizados

1. **MVC/MVVM**: Separación de responsabilidades
   - Model: Modelos de Django
   - View: Componentes de Vue
   - Controller/ViewModel: Pinia Store + API Services

2. **Repository Pattern**: 
   - api.js actúa como repositorio para operaciones del backend

3. **Observer Pattern**: 
   - Reactividad de Vue
   - Watchers en componentes

4. **Factory Pattern**: 
   - Serializers de DRF crean instancias validadas

5. **Strategy Pattern**: 
   - Diferentes validaciones según tipo de registro

## Seguridad

```
┌──────────────────────────────────────┐
│  Medidas de Seguridad Implementadas  │
├──────────────────────────────────────┤
│  ✓ CORS configurado                  │
│  ✓ Validación de datos (frontend)    │
│  ✓ Validación de datos (backend)     │
│  ✓ Sanitización de inputs            │
│  ✓ Validación de formatos            │
│  ✓ Unicidad de CI y NIT              │
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│  Recomendaciones para Producción     │
├──────────────────────────────────────┤
│  □ HTTPS obligatorio                 │
│  □ Autenticación JWT                 │
│  □ Rate Limiting                     │
│  □ Encriptación de datos sensibles   │
│  □ Logs de auditoría                 │
│  □ Respaldos automáticos             │
│  □ Sanitización adicional            │
│  □ Protección CSRF                   │
└──────────────────────────────────────┘
```

## Escalabilidad

### Horizontal
- Frontend: Puede desplegarse en CDN
- Backend: Múltiples instancias con load balancer
- Base de datos: PostgreSQL con replicación

### Vertical
- Optimización de queries
- Caché con Redis
- Indexación de base de datos

## Despliegue

```
┌─────────────────────────────────────────────────────┐
│                 DESARROLLO                          │
│  Frontend: localhost:5173 (Vite dev server)         │
│  Backend: localhost:8000 (Django runserver)         │
└─────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────┐
│                 PRODUCCIÓN                          │
│  Frontend: Netlify / Vercel / S3 + CloudFront       │
│  Backend: AWS EC2 / DigitalOcean / Heroku           │
│  DB: PostgreSQL / MySQL (RDS)                       │
│  Web Server: Nginx / Apache                         │
│  WSGI: Gunicorn / uWSGI                            │
└─────────────────────────────────────────────────────┘
```

## Monitoreo y Logs

```
Frontend:
  - Sentry para errores
  - Google Analytics para métricas
  - Console logs en desarrollo

Backend:
  - Django logging
  - Sentry para errores
  - Logs de acceso de Nginx
  - Métricas de base de datos
```
