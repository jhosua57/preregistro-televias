<template>
  <div class="card max-w-4xl mx-auto">
    <h2 class="text-2xl font-bold text-gray-800 mb-6">Paso 1: Selección Inicial</h2>
    
    <!-- Tipo de Registro -->
    <div class="mb-8">
      <h3 class="text-lg font-semibold text-gray-700 mb-4">Tipo de Registro</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div 
          @click="selectTipoRegistro('persona')"
          :class="[
            'p-6 border-2 rounded-lg cursor-pointer transition-all duration-200',
            tipoRegistro === 'persona' 
              ? 'border-primary-600 bg-primary-50' 
              : 'border-gray-300 hover:border-primary-400'
          ]"
        >
          <div class="flex items-center">
            <RadioButton 
              v-model="tipoRegistro" 
              value="persona" 
              inputId="persona"
              class="mr-3"
            />
            <div>
              <label for="persona" class="font-semibold text-gray-800 cursor-pointer">
                Persona Particular
              </label>
              <p class="text-sm text-gray-600 mt-1">Registro individual para personas naturales</p>
            </div>
          </div>
        </div>
        
        <div 
          @click="selectTipoRegistro('empresa')"
          :class="[
            'p-6 border-2 rounded-lg cursor-pointer transition-all duration-200',
            tipoRegistro === 'empresa' 
              ? 'border-primary-600 bg-primary-50' 
              : 'border-gray-300 hover:border-primary-400'
          ]"
        >
          <div class="flex items-center">
            <RadioButton 
              v-model="tipoRegistro" 
              value="empresa" 
              inputId="empresa"
              class="mr-3"
            />
            <div>
              <label for="empresa" class="font-semibold text-gray-800 cursor-pointer">
                Empresa
              </label>
              <p class="text-sm text-gray-600 mt-1">Registro para empresas públicas o privadas</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Método de Pago -->
    <div class="mb-8">
      <h3 class="text-lg font-semibold text-gray-700 mb-4">Método de Pago</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div 
          @click="selectMetodoPago('prepago')"
          :class="[
            'p-6 border-2 rounded-lg cursor-pointer transition-all duration-200',
            metodoPago === 'prepago' 
              ? 'border-primary-600 bg-primary-50' 
              : 'border-gray-300 hover:border-primary-400'
          ]"
        >
          <div class="flex items-center">
            <RadioButton 
              v-model="metodoPago" 
              value="prepago" 
              inputId="prepago"
              class="mr-3"
            />
            <div>
              <label for="prepago" class="font-semibold text-gray-800 cursor-pointer">
                Prepago
              </label>
              <p class="text-sm text-gray-600 mt-1">Pago anticipado del servicio</p>
            </div>
          </div>
        </div>
        
        <div 
          @click="selectMetodoPago('postpago')"
          :class="[
            'p-6 border-2 rounded-lg cursor-pointer transition-all duration-200',
            metodoPago === 'postpago' 
              ? 'border-primary-600 bg-primary-50' 
              : 'border-gray-300 hover:border-primary-400'
          ]"
        >
          <div class="flex items-center">
            <RadioButton 
              v-model="metodoPago" 
              value="postpago" 
              inputId="postpago"
              class="mr-3"
            />
            <div>
              <label for="postpago" class="font-semibold text-gray-800 cursor-pointer">
                Postpago
              </label>
              <p class="text-sm text-gray-600 mt-1">Pago posterior al uso del servicio</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Botón Siguiente -->
    <div class="flex justify-end">
      <Button 
        label="Siguiente" 
        icon="pi pi-arrow-right" 
        iconPos="right"
        @click="handleNext"
        :disabled="!canProceed"
        class="btn-primary"
      />
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { usePreregistroStore } from '@/stores/preregistro'
import RadioButton from 'primevue/radiobutton'
import Button from 'primevue/button'

const store = usePreregistroStore()

const tipoRegistro = computed({
  get: () => store.tipoRegistro,
  set: (value) => store.setTipoRegistro(value)
})

const metodoPago = computed({
  get: () => store.metodoPago,
  set: (value) => store.setMetodoPago(value)
})

const canProceed = computed(() => store.isStep1Complete)

function selectTipoRegistro(tipo) {
  store.setTipoRegistro(tipo)
}

function selectMetodoPago(metodo) {
  store.setMetodoPago(metodo)
}

function handleNext() {
  if (canProceed.value) {
    store.nextStep()
  }
}
</script>
