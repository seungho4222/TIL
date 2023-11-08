## Passing Props
```md
# Props
: 부모 컴포넌트로부터 자식 컴포넌트로 데이터를 전달하는데 사용되는 속성
- 모든 props는 자식 속성과 부모 속성 사이에 하향식 단방향 바인딩을 형성 (one-way-down binding)
```

```js
// 부모컴포넌트에서 Props 작성
<parentChild my-msg="message"/>
<parentGrandChild :my-msg="myMsg"/>
// => kebab-case 사용

// 1. 문자열 배열 선언
defineProps(['myMsg'])
// 2. 객체 선언  => 권장
defineProps({ myMsg: String })
// 자식컴포넌트에서 선언 후 참조
// => camelCase 사용
```

```md
#emit
: 자식 컴포넌트가 이벤트를 발생시켜 부모 컴포넌트로 데이터를 전달하는 역할의 메서드
```

```js
// 자식컴포넌트에서 이벤트 발신
<button @click="$emit('someEvent')">클릭</button>
<button @click="buttonClick">클릭</button>

// 부모컴포넌트에서 이벤트 수신
<ParentChild @some-event="someCallback" />
// 수신 후 처리할 로직 및 콜백함수 호출
const someCallback = function () { ... }

// emit 이벤트 선언
const emit = defineEmits(['someEvent'])
const buttonClick = function () {
    emit('someEvent', args)
}

/*
- 선언 및 발신 시 : camelCase
- 수신 시 : kebab-case
*/
```

```js
// 참고
defineProps({
    // 여러 타입 허용
    propB: [String, Number],
    // 문자열 필수
    propC: {
        type: String,
        required: true
    },
    // 기본 값을 가지는 숫자형
    propD: {
        type: Number,
        default: 10
    }
})

// 유효성검사 가능
const emit = defineEmits({
    // 유효성 검사 없음
    click: null,
    // submit 이벤트 유효성 검사
    submit: ({ email, password }) => {
        if(email && password) {
            return true
        } else {
            console.warn('submit 이벤트가 옳지 않음')
            return false
        }
    }
})
const submitForm = function (email, password) {
    emit('submit', { email, password })
}
```