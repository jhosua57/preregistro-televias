# Sistema de Preregistro

Sistema de preregistro multi-paso con backend en Django REST Framework y frontend en Vue 3 + Vite + Tailwind CSS + PrimeVue.

## 📋 Características

- ✅ Flujo de registro en 3 pasos
- ✅ Soporte para personas particulares y empresas
- ✅ Validación de formularios en tiempo real
- ✅ Interfaz moderna y responsiva con PrimeVue
- ✅ API RESTful con Django REST Framework
- ✅ Gestión de estado con Pinia
- ✅ Diseño con Tailwind CSS

## 🏗️ Estructura del Proyecto

```
preregistro-system/
├── backend/                    # Django REST Framework
│   ├── config/                # Configuración del proyecto
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── preregistro/           # App principal
│   │   ├── models.py          # Modelos de datos
│   │   ├── serializers.py     # Serializers de DRF
│   │   ├── views.py           # Vistas y lógica de API
│   │   ├── urls.py            # Rutas del API
│   │   └── admin.py           # Panel de administración
│   ├── manage.py
│   └── requirements.txt
│
└── frontend/                  # Vue 3 + Vite
    ├── src/
    │   ├── components/        # Componentes Vue
    │   │   ├── StepIndicator.vue
    │   │   ├── Paso1.vue
    │   │   ├── Paso2.vue
    │   │   └── Paso3.vue
    │   ├── views/             # Vistas principales
    │   │   └── PreregistroView.vue
    │   ├── stores/            # Estado global (Pinia)
    │   │   └── preregistro.js
    │   ├── services/          # Servicios API
    │   │   └── api.js
    │   ├── router/            # Vue Router
    │   │   └── index.js
    │   ├── assets/            # Estilos
    │   │   └── main.css
    │   ├── App.vue
    │   └── main.js
    ├── index.html
    ├── package.json
    ├── vite.config.js
    └── tailwind.config.js
```

## 🚀 Instalación

### Requisitos Previos

- Python 3.10 o superior
- Node.js 18 o superior
- npm o yarn

### Backend (Django)

1. Navegar al directorio del backend:
```bash
cd backend
```

2. Crear y activar un entorno virtual:
```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En Linux/Mac:
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecutar migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Crear superusuario (opcional):
```bash
python manage.py createsuperuser
```

6. Iniciar el servidor de desarrollo:
```bash
python manage.py runserver
```

El backend estará disponible en: `http://localhost:8000`

### Frontend (Vue 3)

1. Navegar al directorio del frontend:
```bash
cd frontend
```

2. Instalar dependencias:
```bash
npm install
```

3. Iniciar el servidor de desarrollo:
```bash
npm run dev
```

El frontend estará disponible en: `http://localhost:5173`

## 📱 Uso del Sistema

### Flujo de Preregistro

#### Paso 1: Selección Inicial
- **Tipo de Registro**: Selecciona entre Persona Particular o Empresa
- **Método de Pago**: Selecciona entre Prepago o Postpago

#### Paso 2: Captura de Datos

**Para Persona Particular:**
- Nombres
- Apellido Paterno
- Apellido Materno
- Dirección
- Carnet de Identidad
- Teléfono
- Celular
- Correo Electrónico

**Para Empresa:**
- Tipo de Empresa (Pública o Privada)
- Nombre de la Empresa
- Responsable
- NIT
- Correo Electrónico
- Dirección
- Teléfono
- Celular

#### Paso 3: Resumen y Confirmación
- Visualiza todos los datos ingresados
- Opción de editar antes de confirmar
- Confirma y envía el preregistro

## 🔌 API Endpoints

### Endpoints Principales

#### Crear Preregistro
```http
POST /api/preregistro/
Content-Type: application/json

{
  "tipo_registro": "persona",  // o "empresa"
  "datos": {
    "nombres": "Juan",
    "apellido_paterno": "Pérez",
    // ... otros campos
  }
}
```

#### Validar Datos
```http
POST /api/validar/
Content-Type: application/json

{
  "tipo_registro": "persona",
  "datos": { ... }
}
```

#### Listar Personas
```http
GET /api/personas/
```

#### Listar Empresas
```http
GET /api/empresas/
```

#### Confirmar Preregistro
```http
PATCH /api/personas/{id}/confirmar/
PATCH /api/empresas/{id}/confirmar/
```

### Respuestas de la API

**Éxito:**
```json
{
  "success": true,
  "message": "Preregistro creado exitosamente",
  "data": { ... }
}
```

**Error:**
```json
{
  "success": false,
  "message": "Error en la validación de datos",
  "errors": { ... }
}
```

## 🎨 Tecnologías Utilizadas

### Backend
- **Django 5.0.1** - Framework web
- **Django REST Framework 3.14.0** - API REST
- **django-cors-headers 4.3.1** - Manejo de CORS
- **SQLite** - Base de datos (desarrollo)

### Frontend
- **Vue 3.4** - Framework JavaScript
- **Vite 5.0** - Build tool
- **Vue Router 4.2** - Enrutamiento
- **Pinia 2.1** - Gestión de estado
- **PrimeVue 3.48** - Componentes UI
- **Tailwind CSS 3.4** - Framework CSS
- **Axios 1.6** - Cliente HTTP

## 🔒 Validaciones

### Backend (Django)
- Validación de formato de email
- Validación de números de teléfono
- Validación de formato de CI y NIT
- Unicidad de CI y NIT
- Validaciones personalizadas en serializers

### Frontend (Vue)
- Validación en tiempo real
- Mensajes de error descriptivos
- Prevención de envío con datos inválidos
- Validación de formato de email

## 🛠️ Configuración

### Variables de Entorno (Backend)

Crear archivo `.env` en el directorio `backend/`:

```env
SECRET_KEY=tu-secret-key-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Configuración CORS

El backend está configurado para aceptar solicitudes desde:
- `http://localhost:5173`
- `http://localhost:3000`
- `http://127.0.0.1:5173`
- `http://127.0.0.1:3000`

## 📊 Panel de Administración

Accede al panel de administración de Django en:
```
http://localhost:8000/admin
```

Funcionalidades:
- Gestión de preregistros de personas
- Gestión de preregistros de empresas
- Filtros por tipo de pago, estado de confirmación, fecha
- Búsqueda por nombre, CI, NIT, email

## 🧪 Testing

### Backend
```bash
cd backend
python manage.py test
```

### Frontend
```bash
cd frontend
npm run test
```

## 📦 Build para Producción

### Frontend
```bash
cd frontend
npm run build
```

Los archivos de producción se generarán en `frontend/dist/`

### Backend
```bash
cd backend
python manage.py collectstatic
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT.

## 👥 Autores

- Sistema desarrollado para gestión de preregistros

## 📞 Soporte

Para soporte o consultas, contacta a través de:
- Email: soporte@ejemplo.com
- Issues: GitHub Issues

---

**Nota**: Este es un proyecto de desarrollo. Para producción, asegúrate de:
- Cambiar `SECRET_KEY` en Django
- Configurar `DEBUG=False`
- Usar una base de datos robusta (PostgreSQL, MySQL)
- Configurar HTTPS
- Implementar autenticación y autorización
- Realizar pruebas de seguridad
