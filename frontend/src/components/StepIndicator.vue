<template>
  <div class="w-full py-6">
    <div class="flex items-center justify-between max-w-3xl mx-auto">
      <!-- Paso 1 -->
      <div class="flex flex-col items-center flex-1">
        <div 
          :class="[
            'step-indicator',
            currentStep === 1 ? 'step-active' : currentStep > 1 ? 'step-completed' : 'step-pending'
          ]"
        >
          <i v-if="currentStep > 1" class="pi pi-check"></i>
          <span v-else>1</span>
        </div>
        <span class="mt-2 text-sm font-medium text-gray-700">Selección</span>
      </div>
      
      <!-- Línea conectora 1 -->
      <div class="flex-1 h-1 mx-2 -mt-8">
        <div 
          class="h-full rounded"
          :class="currentStep > 1 ? 'bg-green-600' : 'bg-gray-300'"
        ></div>
      </div>
      
      <!-- Paso 2 -->
      <div class="flex flex-col items-center flex-1">
        <div 
          :class="[
            'step-indicator',
            currentStep === 2 ? 'step-active' : currentStep > 2 ? 'step-completed' : 'step-pending'
          ]"
        >
          <i v-if="currentStep > 2" class="pi pi-check"></i>
          <span v-else>2</span>
        </div>
        <span class="mt-2 text-sm font-medium text-gray-700">Datos</span>
      </div>
      
      <!-- Línea conectora 2 -->
      <div class="flex-1 h-1 mx-2 -mt-8">
        <div 
          class="h-full rounded"
          :class="currentStep > 2 ? 'bg-green-600' : 'bg-gray-300'"
        ></div>
      </div>
      
      <!-- Paso 3 -->
      <div class="flex flex-col items-center flex-1">
        <div 
          :class="[
            'step-indicator',
            currentStep === 3 ? 'step-active' : 'step-pending'
          ]"
        >
          <span>3</span>
        </div>
        <span class="mt-2 text-sm font-medium text-gray-700">Confirmación</span>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  currentStep: {
    type: Number,
    required: true,
    default: 1
  }
})
</script>
