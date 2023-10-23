## DOM 선택
### 선택 메서드
```js
document.querySelector()
- 요소 한 개 선택
document.querySelectorAll()
- 요소 여러 개 선택

```

## DOM 조작
### classList 메서드
```js
element.classList.add()
- 지정한 클래스 값을 추가
element.classList.remove()
- 지정한 클래스 값을 제거
element.classList.toggle()
- 제거(false반환) or 추가(true반환)

```

### 속성 조작 메서드
```js
element.getAttribute()
- 해당 요소에 지정된 값을 반환(조회)
element.setAttribute(name, value)
- 지정된 요소의 속성 값을 설정
- 추가 or 갱신(변경)
element.removeAttribute()
- 요소에서 지정된 이름을 가진 속성 제거

```

### DOM 요소 조작 메서드
```js
document.createElement(tagName)
- 작성한 tagName의 HTML 요소를 생성하여 반환
Node.appendChild()
- 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
- 추가된 Node 객체를 반환
Node.removeChild()
- DOM에서 자식 Node를 제거
- 제거된 Node를 반환

```