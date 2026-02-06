# 🚀 Guía de Inicio Rápido

## Instalación en 5 minutos

### Prerrequisitos
✅ Python 3.10+  
✅ Node.js 18+  
✅ Git

---

## Opción 1: Inicio Automático (Linux/Mac)

```bash
# 1. Descomprimir el proyecto
tar -xzf preregistro-system.tar.gz
cd preregistro-system

# 2. Ejecutar script de inicio
./start.sh
```

¡Listo! El sistema se iniciará automáticamente.

---

## Opción 2: Inicio Manual

### Backend (Terminal 1)

```bash
# 1. Ir al directorio backend
cd backend

# 2. Crear entorno virtual
python3 -m venv venv

# 3. Activar entorno virtual
# En Linux/Mac:
source venv/bin/activate
# En Windows:
venv\Scripts\activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar migraciones
python manage.py makemigrations
python manage.py migrate

# 6. (Opcional) Crear superusuario para admin
python manage.py createsuperuser

# 7. Iniciar servidor
python manage.py runserver
```

**✅ Backend corriendo en:** http://localhost:8000

### Frontend (Terminal 2)

```bash
# 1. Ir al directorio frontend
cd frontend

# 2. Instalar dependencias
npm install

# 3. Iniciar servidor de desarrollo
npm run dev
```

**✅ Frontend corriendo en:** http://localhost:5173

---

## 🎯 Primeros Pasos

1. **Abre tu navegador** en http://localhost:5173

2. **Completa el formulario:**
   - Paso 1: Selecciona tipo de registro y método de pago
   - Paso 2: Ingresa los datos solicitados
   - Paso 3: Revisa y confirma

3. **Accede al panel de administración:**
   - URL: http://localhost:8000/admin
   - Usa el superusuario que creaste

---

## 🧪 Probar la API

### Con cURL:

```bash
# Crear un preregistro de persona
curl -X POST http://localhost:8000/api/preregistro/ \
  -H "Content-Type: application/json" \
  -d '{
    "tipo_registro": "persona",
    "datos": {
      "nombres": "Juan",
      "apellido_paterno": "Pérez",
      "apellido_materno": "García",
      "carnet_identidad": "1234567 LP",
      "direccion": "Av. Principal 123",
      "telefono": "2123456",
      "celular": "70123456",
      "correo_electronico": "juan@ejemplo.com",
      "metodo_pago": "prepago"
    }
  }'
```

### Con Postman:

1. Importa la colección de endpoints
2. Endpoint: `POST http://localhost:8000/api/preregistro/`
3. Body (JSON): Similar al ejemplo de cURL

---

## 📂 Estructura de Archivos

```
preregistro-system/
├── backend/              # Django Backend
├── frontend/             # Vue 3 Frontend
├── README.md            # Documentación completa
├── API_DOCUMENTATION.md # Documentación de API
├── ARQUITECTURA.md      # Diagramas y arquitectura
└── start.sh            # Script de inicio automático
```

---

## 🔧 Comandos Útiles

### Backend

```bash
# Crear nuevas migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Abrir shell de Django
python manage.py shell

# Ejecutar tests
python manage.py test

# Recolectar archivos estáticos
python manage.py collectstatic
```

### Frontend

```bash
# Iniciar desarrollo
npm run dev

# Build para producción
npm run build

# Preview del build
npm run preview

# Lint
npm run lint
```

---

## 🐛 Solución de Problemas

### Puerto ocupado (Backend)

```bash
# Cambiar puerto en manage.py
python manage.py runserver 8001
```

### Puerto ocupado (Frontend)

```bash
# Vite usa automáticamente el siguiente puerto disponible
# O edita vite.config.js para cambiar el puerto
```

### Error de CORS

Verifica que en `backend/config/settings.py` estén los orígenes correctos:
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:3000",
]
```

### Base de datos bloqueada

```bash
# Elimina la base de datos y vuelve a migrar
rm backend/db.sqlite3
cd backend
python manage.py migrate
```

---

## 📱 Accesos Rápidos

| Servicio | URL | Descripción |
|----------|-----|-------------|
| Frontend | http://localhost:5173 | Aplicación principal |
| Backend API | http://localhost:8000/api | Endpoints REST |
| Admin Django | http://localhost:8000/admin | Panel de administración |
| API Docs | `API_DOCUMENTATION.md` | Documentación detallada |

---

## 🎨 Personalización Rápida

### Cambiar colores (Frontend)

Edita `frontend/tailwind.config.js`:

```javascript
theme: {
  extend: {
    colors: {
      primary: {
        500: '#TU_COLOR_AQUI',
        // ...
      },
    },
  },
}
```

### Cambiar título

Edita `frontend/index.html`:

```html
<title>Tu Título Aquí</title>
```

---

## 📊 Datos de Prueba

### Persona de ejemplo:

```json
{
  "nombres": "María Elena",
  "apellido_paterno": "López",
  "apellido_materno": "Gonzales",
  "carnet_identidad": "9876543 LP",
  "direccion": "Calle 21 de Calacoto #456",
  "telefono": "2234567",
  "celular": "77123456",
  "correo_electronico": "maria@ejemplo.com",
  "metodo_pago": "prepago"
}
```

### Empresa de ejemplo:

```json
{
  "tipo_empresa": "privada",
  "nombre_empresa": "Tech Solutions S.R.L.",
  "responsable": "Carlos Mendoza",
  "nit": "1234567890",
  "correo_electronico": "contacto@techsolutions.com",
  "direccion": "Av. Arce #789",
  "telefono": "2345678",
  "celular": "71234567",
  "metodo_pago": "postpago"
}
```

---

## 🚢 Próximos Pasos

1. ✅ Explora el código fuente
2. ✅ Revisa la documentación de la API
3. ✅ Personaliza los estilos
4. ✅ Agrega nuevas funcionalidades
5. ✅ Despliega en producción

---

## 📚 Recursos Adicionales

- **Vue 3 Docs**: https://vuejs.org/
- **Django Docs**: https://docs.djangoproject.com/
- **DRF Docs**: https://www.django-rest-framework.org/
- **Tailwind CSS**: https://tailwindcss.com/
- **PrimeVue**: https://primevue.org/

---

## 🤝 Soporte

¿Problemas o preguntas?

1. Revisa `README.md` para documentación completa
2. Consulta `API_DOCUMENTATION.md` para detalles de la API
3. Lee `ARQUITECTURA.md` para entender el diseño

---

## ✨ ¡Disfruta construyendo!

El sistema está listo para usar y personalizar según tus necesidades.

**Happy Coding! 🎉**
