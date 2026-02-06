<template>
  <div class="card max-w-4xl mx-auto">
    <h2 class="text-2xl font-bold text-gray-800 mb-6">Paso 3: Resumen y Confirmación</h2>
    
    <Message v-if="successMessage" severity="success" :closable="false" class="mb-6">
      {{ successMessage }}
    </Message>
    
    <Message v-if="errorMessage" severity="error" :closable="false" class="mb-6">
      {{ errorMessage }}
    </Message>
    
    <div class="space-y-6">
      <!-- Información de Selección -->
      <div class="bg-gray-50 p-6 rounded-lg">
        <h3 class="text-lg font-semibold text-gray-800 mb-4">Información de Selección</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <p class="text-sm text-gray-600">Tipo de Registro</p>
            <p class="font-semibold text-gray-800">
              {{ tipoRegistroLabel }}
            </p>
          </div>
          <div>
            <p class="text-sm text-gray-600">Método de Pago</p>
            <p class="font-semibold text-gray-800">
              {{ metodoPagoLabel }}
            </p>
          </div>
        </div>
      </div>
      
      <!-- Datos de Persona -->
      <div v-if="isPersona" class="bg-gray-50 p-6 rounded-lg">
        <h3 class="text-lg font-semibold text-gray-800 mb-4">Datos Personales</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <p class="text-sm text-gray-600">Nombres</p>
            <p class="font-semibold text-gray-800">{{ datosActuales.nombres }}</p>
          </div>
          <div>
            <p class="text-sm text-gray-600">Apellido Paterno</p>
            <p class="font-semibold text-gray-800">{{ datosActuales.apellido_paterno }}</p>
          </div>
          <div>
            <p class="text-sm text-gray-600">Apellido Materno</p>
            <p class="font-semibold text-gray-800">{{ datosActuales.apellido_materno }}</p>
          </div>
          <div>
            <p class="text-sm text-gray-600">Carnet de Identidad</p>
            <p class="font-semibold text-gray-800">{{ datosActuales.carnet_identidad }}</p>
          </div>
          <div>
            <p class="text-sm text-gray-600">Teléfono</p>
            <p class="font-semibold text-gray-800">{{ datosActuales.telefono }}</p>
          </div>
          <div>
            <p class="text-sm text-gray-600">Celular</p>
            <p class="font-semibold text-gray-800">{{ datosActuales.celular }}</p>
          </div>
          <div class="md:col-span-2">
            <p class="text-sm text-gray-600">Correo Electrónico</p>
            <p class="font-semibold text-gray-800">{{ datosActuales.correo_electronico }}</p>
          </div>
          <div class="md:col-span-2">
            <p class="text-sm text-gray-600">Dirección</p>
            <p class="font-semibold text-gray-800">{{ datosActuales.direccion }}</p>
          </div>
        </div>
      </div>
      
      <!-- Datos de Empresa -->
      <div v-else class="bg-gray-50 p-6 rounded-lg">
        <h3 class="text-lg font-semibold text-gray-800 mb-4">Datos de la Empresa</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <p class="text-sm text-gray-600">Tipo de Empresa</p>
            <p class="font-semibold text-gray-800">{{ tipoEmpresaLabel }}</p>
          </div>
          <div>
            <p class="text-sm text-gray-600">Nombre de la Empresa</p>
            <p class="font-semibold text-gray-800">{{ datosActuales.nombre_empresa }}</p>
          </div>
          <div>
            <p class="text-sm text-gray-600">Responsable</p>
            <p class="font-semibold text-gray-800">{{ datosActuales.responsable }}</p>
          </div>
          <div>
            <p class="text-sm text-gray-600">NIT</p>
            <p class="font-semibold text-gray-800">{{ datosActuales.nit }}</p>
          </div>
          <div>
            <p class="text-sm text-gray-600">Teléfono</p>
            <p class="font-semibold text-gray-800">{{ datosActuales.telefono }}</p>
          </div>
          <div>
            <p class="text-sm text-gray-600">Celular</p>
            <p class="font-semibold text-gray-800">{{ datosActuales.celular }}</p>
          </div>
          <div class="md:col-span-2">
            <p class="text-sm text-gray-600">Correo Electrónico</p>
            <p class="font-semibold text-gray-800">{{ datosActuales.correo_electronico }}</p>
          </div>
          <div class="md:col-span-2">
            <p class="text-sm text-gray-600">Dirección</p>
            <p class="font-semibold text-gray-800">{{ datosActuales.direccion }}</p>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Botones -->
    <div class="flex justify-between mt-8">
      <Button 
        label="Anterior" 
        icon="pi pi-arrow-left"
        @click="handlePrevious"
        :disabled="loading"
        class="btn-secondary"
      />
      <div class="flex gap-3">
        <Button 
          label="Editar" 
          icon="pi pi-pencil"
          @click="handleEdit"
          :disabled="loading"
          class="btn-secondary"
        />
        <Button 
          label="Confirmar y Enviar" 
          icon="pi pi-check"
          iconPos="right"
          @click="handleConfirm"
          :loading="loading"
          class="btn-primary"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { usePreregistroStore } from '@/stores/preregistro'
import api from '@/services/api'
import Button from 'primevue/button'
import Message from 'primevue/message'

const store = usePreregistroStore()
const loading = ref(false)
const successMessage = ref('')
const errorMessage = ref('')

const isPersona = computed(() => store.tipoRegistro === 'persona')
const datosActuales = computed(() => store.datosActuales)

const tipoRegistroLabel = computed(() => {
  return store.tipoRegistro === 'persona' ? 'Persona Particular' : 'Empresa'
})

const metodoPagoLabel = computed(() => {
  return store.metodoPago === 'prepago' ? 'Prepago' : 'Postpago'
})

const tipoEmpresaLabel = computed(() => {
  if (!isPersona.value && store.datosEmpresa.tipo_empresa) {
    return store.datosEmpresa.tipo_empresa === 'publica' ? 'Pública' : 'Privada'
  }
  return ''
})

function handlePrevious() {
  store.prevStep()
}

function handleEdit() {
  store.setStep(2)
}

async function handleConfirm() {
  loading.value = true
  successMessage.value = ''
  errorMessage.value = ''
  
  try {
    const payload = store.getPayloadForAPI()
    const response = await api.crearPreregistro(payload.tipo_registro, payload.datos)
    
    if (response.data.success) {
      successMessage.value = '¡Preregistro completado exitosamente! Hemos enviado un correo de confirmación.'
      
      // Resetear el formulario después de 3 segundos
      setTimeout(() => {
        store.resetForm()
      }, 3000)
    }
  } catch (error) {
    console.error('Error al enviar preregistro:', error)
    
    if (error.response && error.response.data) {
      const errors = error.response.data.errors
      if (errors) {
        errorMessage.value = 'Error en la validación: ' + JSON.stringify(errors)
      } else {
        errorMessage.value = error.response.data.message || 'Error al procesar el preregistro'
      }
    } else {
      errorMessage.value = 'Error de conexión. Por favor, intente nuevamente.'
    }
  } finally {
    loading.value = false
  }
}
</script>
