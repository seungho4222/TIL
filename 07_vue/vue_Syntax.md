## Computed Property
```js
> computed()
- 계산된 속성을 정의하는 함수
- 미리 계산된 속성을 사용하여 템플릿에서 단순하게 하고 불필요한 반복 연산을 줄임

const { computed } = Vue
const restOfTodos = computed(() => {
    return todos.value.length > 0 ? 'Y' : 'N'
})
```

```md
# method와 computed 정리
- computed : 의존된 데이터가 변경되면 자동으로 업데이트
- method : 호출해야만 실행됨
```

```md
# Cache (캐시)
- 데이터나 결과를 일시적으로 저장해두는 임시 저장소
- 이후에 같은 데이터나 결과를 다시 계산하지 않고 빠르게 접근할 수 있도록 함
```

## Conditional Rendering
```md
# v-if
- 표현식 값의 T/F를 기반으로 요소를 조건부로 렌더링
- Cheap initial load, expensive toggle

# v-show
- 표현식 값의 T/F를 기반으로 요소의 가시성(visibility)을 전환
- Expensive initial load, cheap toggle

# HTML <template> element
- v-if는 directive이기 때문에 단일요소에만 연결 가능 -> 이 경우 template 요소에 v-if를 사용하면 하나 이상의 요소에 적용 가능
- 페이지가 로드 될 때 렌더링 되지 않지만 JavaScript를 사용하여 나중에 문서에서 사용할 수 있도록 하는 HTML을 보유하기 위한 메커니즘
- "보이지 않는 wrapper 역할"
```

## List Rendering
```md
# v-for
- 소스 데이터를 기반으로 요소 또는 템플릿 블록을 여러 번 렌더링
- 반복 요소에 대한 별칭(alias) 제공

<div v-for="(item, index) in items" :key="item.id"></div>
<div v-for="(value, key, index) in object" :key=고유값></div>

# v-for와 key 반드시 함꼐 사용 !
- 내부 컴포넌트의 상태를 일관되게 유지
- 데이터의 예측 가능한 행동을 유지 (Vue 내부 동작 관련)

# v-for와 v-if 함께 사용 X !
- 동일한 요소에서 v-if가 v-for보다 우선순위 높음
- v-if조건은 v-for 범위의 변수에 접근 불가
- 해결법1 : computed를 활용해 필터링 된 목록으로 반복
- 해결법2 : v-for와 template 요소를 사용하여 v-if를 이동
```

## Watchers
```js
> watch()
- 반응형 데이터를 감시하고, 감시하는 데이터가 변경되면 콜백 함수를 호출

const { watch } = Vue
watch(variable, (newValue, oldValue) => {
    // do something
}, { deep: true})
```

|   | Computed | Watchers |
| :-: | :--------: | :--------: |
|공통점|데이터의 변화를 감지하고 처리|
|동작|의존하는 데이터 속성의 계산된 값 반환|특정 데이터 속성의 변화를 감시하고 작업 수행|
|사용 목적|템플릿 내에서 사용되는 데이터 연산용|데이터 변경에 따른 특정 작업 처리용|
|사용 예시|연산 된 길이, 필터링 된 목록 계산 등|비동기 API 요청, 연관 데이터 업데이트 등|
> computed와 watch 모두 의존(감시)하는 원본 데이터를 직접 변경하지 않음

- [ ] : false
- [x] : true
