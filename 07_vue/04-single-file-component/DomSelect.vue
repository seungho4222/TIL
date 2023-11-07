<template>
    <div>
        <input type="text" ref="input">
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const input = ref(null)

onMounted(() => {
    console.log(input.value)
})

</script>

<style scoped>

</style>