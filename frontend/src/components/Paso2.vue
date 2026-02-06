<template>
  <div class="card max-w-4xl mx-auto">
    <h2 class="text-2xl font-bold text-gray-800 mb-6">
      Paso 2: {{ isPersona ? 'Datos Personales' : 'Datos de la Empresa' }}
    </h2>
    
    <!-- Formulario Persona -->
    <div v-if="isPersona" class="space-y-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="flex flex-col">
          <label for="nombres" class="mb-2 font-semibold text-gray-700">Nombres *</label>
          <InputText 
            id="nombres"
            v-model="formData.nombres"
            placeholder="Ingrese sus nombres"
            :class="{'p-invalid': errors.nombres}"
          />
          <small v-if="errors.nombres" class="p-error">{{ errors.nombres }}</small>
        </div>
        
        <div class="flex flex-col">
          <label for="apellido_paterno" class="mb-2 font-semibold text-gray-700">Apellido Paterno *</label>
          <InputText 
            id="apellido_paterno"
            v-model="formData.apellido_paterno"
            placeholder="Ingrese apellido paterno"
            :class="{'p-invalid': errors.apellido_paterno}"
          />
          <small v-if="errors.apellido_paterno" class="p-error">{{ errors.apellido_paterno }}</small>
        </div>
        
        <div class="flex flex-col">
          <label for="apellido_materno" class="mb-2 font-semibold text-gray-700">Apellido Materno *</label>
          <InputText 
            id="apellido_materno"
            v-model="formData.apellido_materno"
            placeholder="Ingrese apellido materno"
            :class="{'p-invalid': errors.apellido_materno}"
          />
          <small v-if="errors.apellido_materno" class="p-error">{{ errors.apellido_materno }}</small>
        </div>
        
        <div class="flex flex-col">
          <label for="carnet_identidad" class="mb-2 font-semibold text-gray-700">Carnet de Identidad *</label>
          <InputText 
            id="carnet_identidad"
            v-model="formData.carnet_identidad"
            placeholder="Ej: 1234567 LP"
            :class="{'p-invalid': errors.carnet_identidad}"
          />
          <small v-if="errors.carnet_identidad" class="p-error">{{ errors.carnet_identidad }}</small>
        </div>
        
        <div class="flex flex-col">
          <label for="telefono" class="mb-2 font-semibold text-gray-700">Teléfono *</label>
          <InputText 
            id="telefono"
            v-model="formData.telefono"
            placeholder="Ej: 2123456"
            :class="{'p-invalid': errors.telefono}"
          />
          <small v-if="errors.telefono" class="p-error">{{ errors.telefono }}</small>
        </div>
        
        <div class="flex flex-col">
          <label for="celular" class="mb-2 font-semibold text-gray-700">Celular *</label>
          <InputText 
            id="celular"
            v-model="formData.celular"
            placeholder="Ej: 70123456"
            :class="{'p-invalid': errors.celular}"
          />
          <small v-if="errors.celular" class="p-error">{{ errors.celular }}</small>
        </div>
      </div>
      
      <div class="flex flex-col">
        <label for="correo_electronico" class="mb-2 font-semibold text-gray-700">Correo Electrónico *</label>
        <InputText 
          id="correo_electronico"
          v-model="formData.correo_electronico"
          type="email"
          placeholder="ejemplo@correo.com"
          :class="{'p-invalid': errors.correo_electronico}"
        />
        <small v-if="errors.correo_electronico" class="p-error">{{ errors.correo_electronico }}</small>
      </div>
      
      <div class="flex flex-col">
        <label for="direccion" class="mb-2 font-semibold text-gray-700">Dirección *</label>
        <Textarea 
          id="direccion"
          v-model="formData.direccion"
          rows="3"
          placeholder="Ingrese su dirección completa"
          :class="{'p-invalid': errors.direccion}"
        />
        <small v-if="errors.direccion" class="p-error">{{ errors.direccion }}</small>
      </div>
    </div>
    
    <!-- Formulario Empresa -->
    <div v-else class="space-y-6">
      <div class="flex flex-col">
        <label class="mb-2 font-semibold text-gray-700">Tipo de Empresa *</label>
        <div class="flex gap-4">
          <div class="flex items-center">
            <RadioButton 
              v-model="formData.tipo_empresa" 
              value="publica" 
              inputId="publica"
            />
            <label for="publica" class="ml-2">Pública</label>
          </div>
          <div class="flex items-center">
            <RadioButton 
              v-model="formData.tipo_empresa" 
              value="privada" 
              inputId="privada"
            />
            <label for="privada" class="ml-2">Privada</label>
          </div>
        </div>
        <small v-if="errors.tipo_empresa" class="p-error">{{ errors.tipo_empresa }}</small>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="flex flex-col">
          <label for="nombre_empresa" class="mb-2 font-semibold text-gray-700">Nombre de la Empresa *</label>
          <InputText 
            id="nombre_empresa"
            v-model="formData.nombre_empresa"
            placeholder="Razón social de la empresa"
            :class="{'p-invalid': errors.nombre_empresa}"
          />
          <small v-if="errors.nombre_empresa" class="p-error">{{ errors.nombre_empresa }}</small>
        </div>
        
        <div class="flex flex-col">
          <label for="responsable" class="mb-2 font-semibold text-gray-700">Responsable *</label>
          <InputText 
            id="responsable"
            v-model="formData.responsable"
            placeholder="Nombre del responsable"
            :class="{'p-invalid': errors.responsable}"
          />
          <small v-if="errors.responsable" class="p-error">{{ errors.responsable }}</small>
        </div>
        
        <div class="flex flex-col">
          <label for="nit" class="mb-2 font-semibold text-gray-700">NIT *</label>
          <InputText 
            id="nit"
            v-model="formData.nit"
            placeholder="Ej: 1234567890"
            :class="{'p-invalid': errors.nit}"
          />
          <small v-if="errors.nit" class="p-error">{{ errors.nit }}</small>
        </div>
        
        <div class="flex flex-col">
          <label for="correo_electronico_empresa" class="mb-2 font-semibold text-gray-700">Correo Electrónico *</label>
          <InputText 
            id="correo_electronico_empresa"
            v-model="formData.correo_electronico"
            type="email"
            placeholder="contacto@empresa.com"
            :class="{'p-invalid': errors.correo_electronico}"
          />
          <small v-if="errors.correo_electronico" class="p-error">{{ errors.correo_electronico }}</small>
        </div>
        
        <div class="flex flex-col">
          <label for="telefono_empresa" class="mb-2 font-semibold text-gray-700">Teléfono *</label>
          <InputText 
            id="telefono_empresa"
            v-model="formData.telefono"
            placeholder="Ej: 2123456"
            :class="{'p-invalid': errors.telefono}"
          />
          <small v-if="errors.telefono" class="p-error">{{ errors.telefono }}</small>
        </div>
        
        <div class="flex flex-col">
          <label for="celular_empresa" class="mb-2 font-semibold text-gray-700">Celular *</label>
          <InputText 
            id="celular_empresa"
            v-model="formData.celular"
            placeholder="Ej: 70123456"
            :class="{'p-invalid': errors.celular}"
          />
          <small v-if="errors.celular" class="p-error">{{ errors.celular }}</small>
        </div>
      </div>
      
      <div class="flex flex-col">
        <label for="direccion_empresa" class="mb-2 font-semibold text-gray-700">Dirección *</label>
        <Textarea 
          id="direccion_empresa"
          v-model="formData.direccion"
          rows="3"
          placeholder="Dirección de la empresa"
          :class="{'p-invalid': errors.direccion}"
        />
        <small v-if="errors.direccion" class="p-error">{{ errors.direccion }}</small>
      </div>
    </div>
    
    <!-- Botones -->
    <div class="flex justify-between mt-8">
      <Button 
        label="Anterior" 
        icon="pi pi-arrow-left"
        @click="handlePrevious"
        class="btn-secondary"
      />
      <Button 
        label="Siguiente" 
        icon="pi pi-arrow-right" 
        iconPos="right"
        @click="handleNext"
        :disabled="!isFormValid"
        class="btn-primary"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { usePreregistroStore } from '@/stores/preregistro'
import InputText from 'primevue/inputtext'
import Textarea from 'primevue/textarea'
import RadioButton from 'primevue/radiobutton'
import Button from 'primevue/button'

const store = usePreregistroStore()

const isPersona = computed(() => store.tipoRegistro === 'persona')
const errors = ref({})

const formData = computed({
  get: () => {
    if (isPersona.value) {
      return store.datosPersona
    } else {
      return store.datosEmpresa
    }
  },
  set: (value) => {
    if (isPersona.value) {
      store.updateDatosPersona(value)
    } else {
      store.updateDatosEmpresa(value)
    }
  }
})

const isFormValid = computed(() => {
  return store.isStep2Complete && Object.keys(errors.value).length === 0
})

// Validación en tiempo real
watch(formData, () => {
  validateForm()
}, { deep: true })

function validateForm() {
  errors.value = {}
  
  if (isPersona.value) {
    if (!formData.value.nombres) errors.value.nombres = 'Los nombres son requeridos'
    if (!formData.value.apellido_paterno) errors.value.apellido_paterno = 'El apellido paterno es requerido'
    if (!formData.value.apellido_materno) errors.value.apellido_materno = 'El apellido materno es requerido'
    if (!formData.value.carnet_identidad) errors.value.carnet_identidad = 'El carnet de identidad es requerido'
    if (!formData.value.telefono) errors.value.telefono = 'El teléfono es requerido'
    if (!formData.value.celular) errors.value.celular = 'El celular es requerido'
    if (!formData.value.correo_electronico) {
      errors.value.correo_electronico = 'El correo electrónico es requerido'
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.value.correo_electronico)) {
      errors.value.correo_electronico = 'El correo electrónico no es válido'
    }
    if (!formData.value.direccion) errors.value.direccion = 'La dirección es requerida'
  } else {
    if (!formData.value.tipo_empresa) errors.value.tipo_empresa = 'El tipo de empresa es requerido'
    if (!formData.value.nombre_empresa) errors.value.nombre_empresa = 'El nombre de la empresa es requerido'
    if (!formData.value.responsable) errors.value.responsable = 'El responsable es requerido'
    if (!formData.value.nit) errors.value.nit = 'El NIT es requerido'
    if (!formData.value.telefono) errors.value.telefono = 'El teléfono es requerido'
    if (!formData.value.celular) errors.value.celular = 'El celular es requerido'
    if (!formData.value.correo_electronico) {
      errors.value.correo_electronico = 'El correo electrónico es requerido'
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.value.correo_electronico)) {
      errors.value.correo_electronico = 'El correo electrónico no es válido'
    }
    if (!formData.value.direccion) errors.value.direccion = 'La dirección es requerida'
  }
}

function handlePrevious() {
  store.prevStep()
}

function handleNext() {
  validateForm()
  if (isFormValid.value) {
    store.nextStep()
  }
}
</script>
