import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  let id = 0

  // state
  const todos = ref([
    { id: id++, text: 'todo 1', isDone: false},
    { id: id++, text: 'todo 2', isDone: false},
  ])

  // actions
  const addTodo = function (todoText) {
    todos.value.push({
      id: id++,
      text: todoText,
      isDone: false
    })
  }

  const deleteTodo = function (todoId) {
    // todos 배열에서 몇번째 인덱스가 삭제되었는지 검색
    const index = todos.value.findIndex((todo) => todo.id === todoId)
    // 찾은 인덱스 값을 통해 배열에서 요소 삭제
    todos.value.splice(index, 1)
  }
  
  const updateTodo = function (todoId) {
    todos.value = todos.value.map((todo) => {
      if (todo.id === todoId) {
        todo.isDone = !todo.isDone
      }
      return todo
    })
  }

  const doneTodosCount = computed(() => {
    return todos.value.filter((todo) => todo.isDone).length
  })

  return { todos, addTodo, deleteTodo, updateTodo, doneTodosCount }
}, { persist: true})
