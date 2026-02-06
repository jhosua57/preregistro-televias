import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const usePreregistroStore = defineStore('preregistro', () => {
  // Estado
  const currentStep = ref(1)
  const tipoRegistro = ref(null) // 'persona' | 'empresa'
  const metodoPago = ref(null) // 'prepago' | 'postpago'
  
  // Datos del formulario persona
  const datosPersona = ref({
    nombres: '',
    apellido_paterno: '',
    apellido_materno: '',
    direccion: '',
    carnet_identidad: '',
    telefono: '',
    celular: '',
    correo_electronico: '',
  })
  
  // Datos del formulario empresa
  const datosEmpresa = ref({
    tipo_empresa: null, // 'publica' | 'privada'
    nombre_empresa: '',
    responsable: '',
    nit: '',
    correo_electronico: '',
    direccion: '',
    telefono: '',
    celular: '',
  })
  
  // Computed
  const datosActuales = computed(() => {
    if (tipoRegistro.value === 'persona') {
      return { ...datosPersona.value, metodo_pago: metodoPago.value }
    } else if (tipoRegistro.value === 'empresa') {
      return { ...datosEmpresa.value, metodo_pago: metodoPago.value }
    }
    return {}
  })
  
  const isStep1Complete = computed(() => {
    return tipoRegistro.value !== null && metodoPago.value !== null
  })
  
  const isStep2Complete = computed(() => {
    if (tipoRegistro.value === 'persona') {
      return (
        datosPersona.value.nombres &&
        datosPersona.value.apellido_paterno &&
        datosPersona.value.apellido_materno &&
        datosPersona.value.direccion &&
        datosPersona.value.carnet_identidad &&
        datosPersona.value.telefono &&
        datosPersona.value.celular &&
        datosPersona.value.correo_electronico
      )
    } else if (tipoRegistro.value === 'empresa') {
      return (
        datosEmpresa.value.tipo_empresa &&
        datosEmpresa.value.nombre_empresa &&
        datosEmpresa.value.responsable &&
        datosEmpresa.value.nit &&
        datosEmpresa.value.correo_electronico &&
        datosEmpresa.value.direccion &&
        datosEmpresa.value.telefono &&
        datosEmpresa.value.celular
      )
    }
    return false
  })
  
  // Acciones
  function setStep(step) {
    currentStep.value = step
  }
  
  function nextStep() {
    if (currentStep.value < 3) {
      currentStep.value++
    }
  }
  
  function prevStep() {
    if (currentStep.value > 1) {
      currentStep.value--
    }
  }
  
  function setTipoRegistro(tipo) {
    tipoRegistro.value = tipo
  }
  
  function setMetodoPago(metodo) {
    metodoPago.value = metodo
  }
  
  function updateDatosPersona(datos) {
    datosPersona.value = { ...datosPersona.value, ...datos }
  }
  
  function updateDatosEmpresa(datos) {
    datosEmpresa.value = { ...datosEmpresa.value, ...datos }
  }
  
  function resetForm() {
    currentStep.value = 1
    tipoRegistro.value = null
    metodoPago.value = null
    datosPersona.value = {
      nombres: '',
      apellido_paterno: '',
      apellido_materno: '',
      direccion: '',
      carnet_identidad: '',
      telefono: '',
      celular: '',
      correo_electronico: '',
    }
    datosEmpresa.value = {
      tipo_empresa: null,
      nombre_empresa: '',
      responsable: '',
      nit: '',
      correo_electronico: '',
      direccion: '',
      telefono: '',
      celular: '',
    }
  }
  
  function getPayloadForAPI() {
    return {
      tipo_registro: tipoRegistro.value,
      datos: datosActuales.value
    }
  }
  
  return {
    // Estado
    currentStep,
    tipoRegistro,
    metodoPago,
    datosPersona,
    datosEmpresa,
    
    // Computed
    datosActuales,
    isStep1Complete,
    isStep2Complete,
    
    // Acciones
    setStep,
    nextStep,
    prevStep,
    setTipoRegistro,
    setMetodoPago,
    updateDatosPersona,
    updateDatosEmpresa,
    resetForm,
    getPayloadForAPI,
  }
})
