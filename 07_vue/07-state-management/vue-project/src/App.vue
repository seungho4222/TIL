<template>
  <div>
    <h1>Todo PJT</h1>
    <h2>완료된 Todo : {{ store.doneTodosCount }}</h2>
    <TodoForm />
    <TodoList />
  </div>
</template>

<script setup>
import TodoForm from '@/components/TodoForm.vue';
import TodoList from '@/components/TodoList.vue';

import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()

</script>

<style scoped>

</style>

<!-- <template>
  <div>
    <p>{{ inputText }}</p>
    <input type="text" @input="onInput" :value="inputText">
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()

const inputText = ref("안녕하세요")
const onInput = function (event) {
  inputText.value = event.currentTarget.value
}

</script>

<style scoped>

</style> -->