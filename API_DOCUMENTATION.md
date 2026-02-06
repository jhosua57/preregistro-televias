# Documentación de API - Sistema de Preregistro

## Base URL
```
http://localhost:8000/api
```

## Autenticación
Actualmente el sistema no requiere autenticación. Para producción se recomienda implementar JWT o Token Authentication.

---

## Endpoints

### 1. Crear Preregistro

Crea un nuevo preregistro (persona o empresa).

**Endpoint:** `POST /preregistro/`

**Request Body:**
```json
{
  "tipo_registro": "persona",  // "persona" | "empresa"
  "datos": {
    // Para persona:
    "nombres": "Juan Carlos",
    "apellido_paterno": "Pérez",
    "apellido_materno": "García",
    "direccion": "Av. 6 de Agosto #1234",
    "carnet_identidad": "1234567 LP",
    "telefono": "2123456",
    "celular": "70123456",
    "correo_electronico": "juan@ejemplo.com",
    "metodo_pago": "prepago"  // "prepago" | "postpago"
  }
}
```

**Response (Success - 201):**
```json
{
  "success": true,
  "message": "Preregistro creado exitosamente",
  "tipo_registro": "persona",
  "data": {
    "id": 1,
    "nombres": "Juan Carlos",
    "apellido_paterno": "Pérez",
    "apellido_materno": "García",
    "direccion": "Av. 6 de Agosto #1234",
    "carnet_identidad": "1234567 LP",
    "telefono": "2123456",
    "celular": "70123456",
    "correo_electronico": "juan@ejemplo.com",
    "metodo_pago": "prepago",
    "confirmado": false,
    "fecha_registro": "2024-02-05T10:30:00Z"
  },
  "id": 1
}
```

**Response (Error - 400):**
```json
{
  "success": false,
  "message": "Error en la validación de datos",
  "errors": {
    "correo_electronico": ["Ingrese una dirección de correo electrónico válida."],
    "carnet_identidad": ["Este campo es requerido."]
  }
}
```

---

### 2. Validar Datos

Valida los datos del formulario sin guardarlos en la base de datos.

**Endpoint:** `POST /validar/`

**Request Body:**
```json
{
  "tipo_registro": "empresa",
  "datos": {
    "tipo_empresa": "privada",  // "publica" | "privada"
    "nombre_empresa": "Empresa ABC S.R.L.",
    "responsable": "María López",
    "nit": "1234567890",
    "correo_electronico": "contacto@empresa.com",
    "direccion": "Calle 21 #456",
    "telefono": "2234567",
    "celular": "77123456",
    "metodo_pago": "postpago"
  }
}
```

**Response (Success - 200):**
```json
{
  "success": true,
  "message": "Datos válidos",
  "data": {
    "tipo_empresa": "privada",
    "nombre_empresa": "Empresa ABC S.R.L.",
    // ... resto de datos validados
  }
}
```

---

### 3. Listar Personas

Obtiene la lista de todos los preregistros de personas particulares.

**Endpoint:** `GET /personas/`

**Query Parameters:**
- `page` (opcional): Número de página (default: 1)
- `page_size` (opcional): Cantidad de resultados por página (default: 10)
- `metodo_pago` (opcional): Filtrar por método de pago ("prepago" | "postpago")
- `confirmado` (opcional): Filtrar por estado de confirmación (true | false)

**Example Request:**
```
GET /personas/?page=1&metodo_pago=prepago&confirmado=false
```

**Response (Success - 200):**
```json
{
  "count": 25,
  "next": "http://localhost:8000/api/personas/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "nombres": "Juan Carlos",
      "apellido_paterno": "Pérez",
      "apellido_materno": "García",
      "direccion": "Av. 6 de Agosto #1234",
      "carnet_identidad": "1234567 LP",
      "telefono": "2123456",
      "celular": "70123456",
      "correo_electronico": "juan@ejemplo.com",
      "metodo_pago": "prepago",
      "confirmado": false,
      "fecha_registro": "2024-02-05T10:30:00Z"
    }
    // ... más resultados
  ]
}
```

---

### 4. Obtener Persona por ID

Obtiene los detalles de un preregistro de persona específico.

**Endpoint:** `GET /personas/{id}/`

**Response (Success - 200):**
```json
{
  "id": 1,
  "nombres": "Juan Carlos",
  "apellido_paterno": "Pérez",
  "apellido_materno": "García",
  "direccion": "Av. 6 de Agosto #1234",
  "carnet_identidad": "1234567 LP",
  "telefono": "2123456",
  "celular": "70123456",
  "correo_electronico": "juan@ejemplo.com",
  "metodo_pago": "prepago",
  "confirmado": false,
  "fecha_registro": "2024-02-05T10:30:00Z"
}
```

---

### 5. Confirmar Preregistro de Persona

Marca un preregistro de persona como confirmado.

**Endpoint:** `PATCH /personas/{id}/confirmar/`

**Response (Success - 200):**
```json
{
  "success": true,
  "message": "Preregistro confirmado exitosamente",
  "data": {
    "id": 1,
    "nombres": "Juan Carlos",
    // ... resto de datos
    "confirmado": true
  }
}
```

---

### 6. Listar Empresas

Obtiene la lista de todos los preregistros de empresas.

**Endpoint:** `GET /empresas/`

**Query Parameters:**
- `page` (opcional): Número de página
- `page_size` (opcional): Cantidad de resultados por página
- `tipo_empresa` (opcional): Filtrar por tipo ("publica" | "privada")
- `metodo_pago` (opcional): Filtrar por método de pago
- `confirmado` (opcional): Filtrar por estado de confirmación

**Response:** Similar a listar personas

---

### 7. Obtener Empresa por ID

**Endpoint:** `GET /empresas/{id}/`

**Response (Success - 200):**
```json
{
  "id": 1,
  "tipo_empresa": "privada",
  "nombre_empresa": "Empresa ABC S.R.L.",
  "responsable": "María López",
  "nit": "1234567890",
  "correo_electronico": "contacto@empresa.com",
  "direccion": "Calle 21 #456",
  "telefono": "2234567",
  "celular": "77123456",
  "metodo_pago": "postpago",
  "confirmado": false,
  "fecha_registro": "2024-02-05T11:15:00Z"
}
```

---

### 8. Confirmar Preregistro de Empresa

**Endpoint:** `PATCH /empresas/{id}/confirmar/`

**Response:** Similar a confirmar persona

---

## Códigos de Estado HTTP

- `200 OK` - Solicitud exitosa
- `201 Created` - Recurso creado exitosamente
- `400 Bad Request` - Error en los datos enviados
- `404 Not Found` - Recurso no encontrado
- `500 Internal Server Error` - Error del servidor

---

## Validaciones

### Persona Particular
- **nombres**: Requerido, mínimo 2 caracteres
- **apellido_paterno**: Requerido, mínimo 2 caracteres
- **apellido_materno**: Requerido, mínimo 2 caracteres
- **carnet_identidad**: Requerido, único, formato alfanumérico con guiones
- **telefono**: Requerido, formato numérico 7-15 dígitos
- **celular**: Requerido, formato numérico 7-15 dígitos
- **correo_electronico**: Requerido, formato email válido
- **direccion**: Requerido
- **metodo_pago**: Requerido, valores: "prepago" | "postpago"

### Empresa
- **tipo_empresa**: Requerido, valores: "publica" | "privada"
- **nombre_empresa**: Requerido, mínimo 3 caracteres
- **responsable**: Requerido, mínimo 3 caracteres
- **nit**: Requerido, único, mínimo 5 caracteres, solo números y guiones
- **correo_electronico**: Requerido, formato email válido
- **telefono**: Requerido, formato numérico 7-15 dígitos
- **celular**: Requerido, formato numérico 7-15 dígitos
- **direccion**: Requerido
- **metodo_pago**: Requerido, valores: "prepago" | "postpago"

---

## Ejemplos de Uso con cURL

### Crear preregistro de persona:
```bash
curl -X POST http://localhost:8000/api/preregistro/ \
  -H "Content-Type: application/json" \
  -d '{
    "tipo_registro": "persona",
    "datos": {
      "nombres": "Juan Carlos",
      "apellido_paterno": "Pérez",
      "apellido_materno": "García",
      "direccion": "Av. 6 de Agosto #1234",
      "carnet_identidad": "1234567 LP",
      "telefono": "2123456",
      "celular": "70123456",
      "correo_electronico": "juan@ejemplo.com",
      "metodo_pago": "prepago"
    }
  }'
```

### Validar datos:
```bash
curl -X POST http://localhost:8000/api/validar/ \
  -H "Content-Type: application/json" \
  -d '{
    "tipo_registro": "persona",
    "datos": {
      "nombres": "María",
      "correo_electronico": "invalido"
    }
  }'
```

### Listar personas:
```bash
curl http://localhost:8000/api/personas/
```

### Confirmar preregistro:
```bash
curl -X PATCH http://localhost:8000/api/personas/1/confirmar/
```

---

## Notas Adicionales

1. **CORS**: El backend está configurado para aceptar solicitudes desde localhost:5173 y localhost:3000
2. **Paginación**: Por defecto, las listas retornan 10 elementos por página
3. **Fechas**: Todas las fechas están en formato ISO 8601 (UTC)
4. **IDs únicos**: CI y NIT deben ser únicos en la base de datos
5. **Confirmación**: Una vez confirmado, un preregistro puede considerarse como procesado

---

## Próximas Mejoras

- [ ] Autenticación con JWT
- [ ] Límite de rate limiting
- [ ] Webhooks para notificaciones
- [ ] Exportación a CSV/Excel
- [ ] Búsqueda avanzada con filtros múltiples
- [ ] Soft delete para preregistros
- [ ] Historial de cambios
- [ ] Validación de duplicados antes de guardar
