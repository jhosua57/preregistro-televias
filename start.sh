#!/bin/bash

echo "🚀 Iniciando Sistema de Preregistro..."
echo ""

# Colores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Backend
echo -e "${BLUE}📦 Iniciando Backend (Django)...${NC}"
cd backend

# Verificar si existe el entorno virtual
if [ ! -d "venv" ]; then
    echo "Creando entorno virtual..."
    python3 -m venv venv
fi

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
echo "Instalando dependencias de Python..."
pip install -r requirements.txt -q

# Ejecutar migraciones
echo "Ejecutando migraciones..."
python manage.py makemigrations
python manage.py migrate

# Iniciar servidor Django en background
echo -e "${GREEN}✅ Backend iniciado en http://localhost:8000${NC}"
python manage.py runserver &
DJANGO_PID=$!

cd ..

# Frontend
echo ""
echo -e "${BLUE}📦 Iniciando Frontend (Vue 3)...${NC}"
cd frontend

# Instalar dependencias si no existen
if [ ! -d "node_modules" ]; then
    echo "Instalando dependencias de Node..."
    npm install
fi

# Iniciar servidor Vite
echo -e "${GREEN}✅ Frontend iniciado en http://localhost:5173${NC}"
npm run dev &
VITE_PID=$!

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}✨ Sistema iniciado correctamente!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo -e "Frontend: ${BLUE}http://localhost:5173${NC}"
echo -e "Backend:  ${BLUE}http://localhost:8000${NC}"
echo -e "Admin:    ${BLUE}http://localhost:8000/admin${NC}"
echo ""
echo "Presiona Ctrl+C para detener los servidores"

# Esperar a que se presione Ctrl+C
wait $DJANGO_PID $VITE_PID
