<template>
  <div class="min-h-screen bg-gray-50 py-8 px-4">
    <div class="max-w-6xl mx-auto">
      <!-- Header -->
      <div class="text-center mb-8">
        <h1 class="text-4xl font-bold text-gray-900 mb-2">Sistema de Preregistro</h1>
        <p class="text-gray-600">Complete el formulario en 3 sencillos pasos</p>
      </div>
      
      <!-- Step Indicator -->
      <StepIndicator :current-step="currentStep" />
      
      <!-- Steps Content -->
      <div class="mt-8">
        <Transition name="fade" mode="out-in">
          <Paso1 v-if="currentStep === 1" key="paso1" />
          <Paso2 v-else-if="currentStep === 2" key="paso2" />
          <Paso3 v-else-if="currentStep === 3" key="paso3" />
        </Transition>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { usePreregistroStore } from '@/stores/preregistro'
import StepIndicator from '@/components/StepIndicator.vue'
import Paso1 from '@/components/Paso1.vue'
import Paso2 from '@/components/Paso2.vue'
import Paso3 from '@/components/Paso3.vue'

const store = usePreregistroStore()
const currentStep = computed(() => store.currentStep)
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
