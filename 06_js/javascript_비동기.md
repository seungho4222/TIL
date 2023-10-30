## 1. 비동기

#### synchronous (동기)
- 프로그램의 실행 흐름이 순차적으로 진행 (하나의 작업이 완료된 후에 다음 작업이 실행되는 방식)

#### Asynchronous (비동기)
- 프로그램의 실행 흐름이 순차적이지 않으며, 작업이 완료되기를 기다리지 않고 다음 작업이 실행되는 방식 (작업의 완료 여부를 신경 쓰지 않고 동시에 다른 작업들을 수행할 수 있음)
- 특징
  - 병력적 수행
  - 당장 처리를 완료할 수 없고 시간이 필요한 작업들은 별도로 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리

#### Thread 란?
- 작업을 처리할 때 실제로 작업을 수행하는 주체로, multi-thread라면 업무를 수행할 수 있는 주체가 여러 개라는 의미

```js 정리
- JavaScript는 한 번에 하나의 작업을 수행하는 Single Thread 언어로 동기적 처리를 진행
- 하지만 부라우저 환경에서는 Web API에서 처리된 작업이 지속적으로 Task Queue를 거쳐 Event Loop에 의해 Call Stack에 들어와 순차적으로 실행됨으로써 비동기 작업이 가능한 환경이 됨
```

## 2. AJAX

#### AJAX (Asynchronous JavaScript + XML)
- JavaScript의 비동기 구조와 XML 객체를 활용해 비동기적으로 서버와 통신하여 웹 페이지의 일부분만을 업데이트하는 웹 개발 기술

#### XHR 객체 (XMLHttpRequest 객체)
- 서버와 상호작용할 때 사용하며 페이지의 새로고침없이도 URL에서 데이터를 가져올 수 있음

#### Axios
- JavaScript에서 사용되는 Promise 기반 HTTP 클라이언트 라이브러리 (서버와의 HTTP 요청과 응답을 간편하게 처리할 수 있도록 도와주는 도구)
  
```js
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
axios({
    method: 'post',
    url: '/user/12345',
    data: {
        firstName: 'Seungho',
        lastName: 'Lee'
    }
})
  .then(요청에 성공하면 수행할 콜백함수)
  .catch(요청에 실패하면 수행할 콜백함수)
```

```js 정리
- axios는 브라우저에서 비동기로 데이터 통신을 가능하게 하는 라이브러리
    - 브라우저를 위해 XMLHttpRequest 생성
- 같은 방식으로 DRF로 만든 API 서버로 요청을 보내서 데이터를 받아온 후 처리할 수 있도록 함
```

## 3. Callback과 Promise

#### 비동기 콜백
- 비동기적으로 처리되는 작업이 완료되었을 때 실행되는 함수
- 연쇄적으로 발생하는 비동기 작업을 순차적으로 동작할 수 있게 함
- :star: 작업의 순서와 동작을 제어하거나 결과를 처리하는 데 사용

#### Promise
- JavaScript에서 비동기 작업의 결과를 나타내는 객체
- :star: 비동기 작업이 완료되었을 때 결과 값을 반환하거나, 실패 시 에러를 처리할 수 있는 기능을 제공

```js
// promise 방식

work1()
  .then((result1) => {
    // work2
    return result2
  })
  .then((result2) => {
    // work3
    return result3
  })
  .catch((error) => {
    // error handling
  })
```

- then 메서드 chaining의 목적
  - 비동기 작업의 "순차적인" 처리 가능
  - 코드를 보다 직관적이고 가독성 좋게 작성할 수 있도록 도움

-  then 메서드 chaining의 장점
   1. 가동성
   2. 에러 처리
   3. 유연성
   4. 코드 관리

```js 정리
// Promise가 보장하는 것(vs 비동기 콜백)
1. 콜백 함수는 JavasScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출되지 않음
    - 반면 Promise callback 함수는 Event Queue에 배치되는 엄격한 순서로 호출됨
2. 비동기 작업이 성공하거나 실패한 뒤에 .then() 메서드를 이용하여 추가한 경우에도 호출 순서를 보장하며 동작
3. .then()을 여러 번 사용하여 여러 개의 callback 함수를 추가할 수 있음
    - 각각의 callback은 주어진 순서대로 하나하나 실행하게 됨
    - Chaining은 Promise의 가장 뛰어난 장점
```