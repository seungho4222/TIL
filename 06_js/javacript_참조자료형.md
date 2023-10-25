### 함수
```js
# 함수 정의
- 선언식
function add (num1, num2) {
    return num1 + num2
} // 익명함수 X, 호이스팅 O

- 표현식
const sub = function (num1, num2) {
    return num1 - num2
} // 익명함수 O, 호이스팅 X
```

```js
# 전개 구문
- 배열이나 문자열과 같이 반복 가능한 항목을 펼치는 것
function myFunc(x, y, z) {
    return x + y + z
}

let numbers = [1, 2 ,3]

console.log(myFunc(...numbers)) // 6
```

```js
# 화살표 함수 표현식
- 함수 표현식의 간결한 표현법
const arrow = function (name) { return `hello, ${name}` }
const arrow = name => `hello, ${name}`

1. 인자가 없다면 () or _로 표시 가능
const noArgs = () => 'No'

2. object를 return 한다면 return을 명시적으로 작성 필요
const returnObj1 = () => { return { key: 'value' } }

3. return을 작성하지 않으려면 객체를 소괄호로 감싸야 함
const returnObj2 = () => ({ key: 'value' })
```


### 객체
```js
# this
- 단순 호출 : 전역객체 대상
- 메서드 호출 : 메서드를 호출한 객체
- 중첩된 함수에서의 this
    => 화살표 함수는 자신만의 this를 가지지 않기 때문에 외부 함수에서의 this 값을 가져옴
```

```js
# 추가 객체 문법
- 변수 이름 같으면 생략
const name = 'Lee'
const age = 28
const user = {
    name,
    age,
}

- 메서드 선언시 function 생략
const myObj = {
    myFunc() {
        return 'Ohayo'
    }
}

- []로 둘러싸면 변수 값 사용 가능
const prefix = 'hi'
const bag = {
    [prefix]: 5
}

- 구조 분해 할당
const userInfo = {
    firstName: 'Lee',
    userId: 'five',
    email: 'ssafy@day.com'
}
const {firstName, userId, email} = userInfo

- Object with '전개 구문'
    - 객체 복사(얕은 복사에 활용 가능)
const obj = {b:2, c:3}
const newObj = {a:1, ...obj, d:4}

- 유용한 객체 메서드
const profile = {
    name: 'Lee',
    age: 28,
}

console.log(Object.keys(profile)) // ['name', 'age']
console.log(Object.keys(profile)) // ['Lee', '28']

- Optional chaining('?.')
    1. 에러없이 접근 가능
    2. 에러 발생 시 undefined 반환
    3. Optional chaining이 없다면 '&&' 연산자 사용
```

```js
# JSON (JavaScript Object Notation)
- Object -> JSON
const objToJson = JSON.stringify(jsObject)

- JSON -> Object
const jsonToObj = JSON.parse(objToJson)
```

```js
# new 연산자
function Member(name, age) {
    this.name = name
    this.age = age
}

const member1 = new Member('Lee', 28)
```


### 배열
```js
# 배열 구조
- 대괄호([])를 이용해 작성
- length 속성을 사용해 개수 체크
const names = ['Lee', 'Park']
console.log(names.length) // 2
```

```js
# 주요 메서드
- push / pop
    => 배열 끝 요소 추가, 제거

- unshift / shift
    => 배열 앞 요소 추가, 제거
```

```js
# Array Helper Methods
- forEach
    => 인자로 주어진 함수(콜백함수)를 배열 요소 각각에 대해 실행
array.forEach(function (item, index, array) { // do something
})

- map
    => 배열 내의 모든 요소 각각에 대해 함수(콜백함수)를 호출하고, 함수 호출 결과를 모아 새로운 배열을 반환
const newArr = array.map(function (item, index, array) { // do something
})

- filter, find, some, every ...
```

```js
# 배열 순회 종합
- for loop
    : 배열의 idx를 이용하여 각 요소에 접근
    : break, continue 사용 가능
- for ... of
    : 배열 요소에 바로 접근 가능
    : break, continue 사용 가능
- forEach (*사용 권장)
    : callback 함수 이용하여 각 요소 조작 용이
    : break, continue 사용 불가

```