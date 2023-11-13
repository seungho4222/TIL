<template>
  <div>
    <TodoListItem 
      v-for="todo in store.todos"
      :key="todo.id"
      :todo-data="todo"
    />
  </div>
</template>

<script setup>
import TodoListItem from '@/components/TodoListItem.vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

</script>

<style scoped>

</style>