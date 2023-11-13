## State ManageMent (상태관리)
> Vue 컴포넌트는 이미 반응형 상태를 관리하고 있음 (상태 === 데이터)
```md
# 상태(State)
- 앱 구동에 필요한 기본 데이터

# 뷰(View)
- 상태를 선언적으로 매핑하여 시각화

# 기능(Actions)
- 뷰에서 사용자 입력에 대해 반응적으로 상태를 변경할 수 있게 정의된 동작

> "단방향 데이터 흐름"의 간단한 표현
```

## Pinia
> Vue의 공식 상태 관리 라이브러리
```md
# 구성 요소
1. store
  - 중앙 저장소
  - 모든 컴포넌트가 공유하는 상태, 기능 등이 작성됨
2. state
  - 반응형 상태(데이터)
  - ref() === state
3. getters
  - 계산된 값
  - computed() === getters
4. actions
  - 메서드
  - function() === actions
5. plugin
  - 애플리케이션의 상태 관리에 필요한 추가 기능을 제공하거나 확장하는 도구나 모듈
  - 애플리케이션의 상태 관리를 더욱 간편하고 유연하게 만들어주며 패키지 매니저로 설치 이후 별도 설정을 통해 추가 됨
```

```js
// store 사용
import { useCounterStore} from '@/stores/counter'

const store = useCounterStore()

// input 데이터 초기화 방법
<template>
  <form ... ref="formElem"></form>
</template>

<script setup>
  const formElem = ref(null)
  const createTodo = function (todoText) {
    store.addTodo(todoText)
    formElem.value.reset()
  }
</script>

// Todo 삭제
const deleteTodo = function (todoId) {
  const index = todos.value.findIndex((todo) => todo.id === todoId)
  todos.value.splice(index, 1)
}

// getters 예시
const doneTodosCount = computed() => {
  return todos.value.filter((todo) => todo.isDone).length
}
```

```js
# Local Storage : 브라우저 내에 key-value 쌍을 저장하는 웹 스토리지 객체
// 설치 및 등록
npm i pinia-plugin-persistedstate

// main.js
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

const pinia = createPinia()

pinia.use(piniaPluginPersistedstate)

// app.use(createPinia())
app.use(pinia)

// stores/counter.js
export const useCounterStore = defineStore('counter', () => {
  ...
  return { todos, addTodo, deleteTodo, updateTodo, doneTodosCount }
}, { persist: true })
```