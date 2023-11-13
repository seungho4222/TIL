<template>
  <div>
    <span 
      @click="store.updateTodo(todoData.id)"
      :class="{ 'is-done': todoData.isDone }"
    >
      {{ todoData.text }}
    </span>
    <button @click="store.deleteTodo(todoData.id)">XX</button>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
defineProps({
  todoData: Object
})

const store = useCounterStore()
</script>

<style scoped>
.is-done {
  text-decoration: line-through;
}

</style>