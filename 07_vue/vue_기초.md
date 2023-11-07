## Front-end Development
```md
- 웹사이트와 웹 애플리케이션의 사용자 인터페이스(UI)와 사용자 경험(UX)을 만들고 디자인 하는 것
  * HTML, CSS JavaScript 등을 활용하여 사용자가 직접 상호작용하는 부분을 개발
```

- Client-side frameworks
  - 클라이언트 측에서 UI와 상호작용을 개발하기 위해 사용되는 Javascript 기반 프레임워크

- Single Page Application (SPA)
  - 페이지 한 개로 구성된 웹 애플리케이션
  - 웹 애플리케이션의 초기 로딩 후 새로운 페이지 요청 없이 동적으로 화면을 갱신하며 사용자와 상호작용하는 웹 애플리케이션 (CSR 방식)

- Client-side Redndering (CSR)
  - 클라이언트에서 화면을 렌더링 하는 방식
  1. 브라우저는 페이지에 필요한 최소한의 HTML 페이지와 JavaScript를 다운로드
  2. 그런 다음 JavaScript를 사용하여 DOM을 업데이트하고 페이지를 렌더링

```md
# CSR 장점
1. 빠른 속도
  - 페이지의 일부를 다시 렌더링할 수 있으므로 동일한 웹 사이트의 다른 페이지로 이동하는 것이 일반적으로 더 빠름
  - 서버로 전송되는 데이터의 양을 최소화

2. 사용자 경험
  - 새로고침이 발생하지 않아 네이티브 앱과 유사한 사용자 경험을 제공

3. Front-end와 Back-end의 명확한 분리
  - Front-end는 UI 렌더링 및 사용자 상호 작용 처리를 담당 & Back-end는 데이터 및 API 제공을 담당
  - 대규모 애플리케이션을 더 쉽게 개발하고 유지 관리 가능

# CSR 단점
1. 초기 구동속도가 느림
  - 전체 페이지를 보기 전에 약간의 지연을 느낄 수 있음
  - JavaScript가 다운로드, 구문 분석 및 실행될 때까지 페이지가 완전히 렌더링 되지 않기 때문

2. SEO(검색 엔진 최적화) 문제
  - 페이지를 나중에 그려 나가는 것이기 때문에 검색에 잘 노출되지 않을 수 있음 
```

## Vue
```md
# 핵심 기능
1. 선언적 렌더링 (Declarative Rendering)
  - HTML을 확장하는 템플릿 구문을 사용하여 HTML이 JavaScript 데이터를 기반으로 어떻게 보이는지 설명할 수 있음
2. 반응형 (Reactivity)
  - JavaScript 상태 변경사항을 자동으로 추적하고 변경사항이 발생할 때 DOM을 효율적으로 업데이트
```

## SFC
```md
# Component
: 재사용 가능한 코드 블록
- UI를 독립적이고 재사용 가능한 일부분으로 분할하고 각 부분을 개별적으로 다룰 수 있음
- 그러면 자연스럽게 앱은 중첩된 Component의 트리로 구성됨

# Single-File Components (SFC)
: 컴포넌트의 템플릿, 로직 및 스타일을 하나의 파일로 묶어낸 특수한 파일 형식 (.vue 파일)
- vite 프로젝트 생성
  1. npm create vue@latest
    - 프로젝트 명 및 세부 설정 체크
  2. cd vue-project
    - 경로 이동
  3. npm install
    - 패키지 설치
  4. npm run dev
    - 프로젝트 서버 실행

# Node Package Manager (NPM)
: Node.js의 기본 패키지 관리자
> Node.js란 Chrome의 V8 JavaScript 엔진을 기반으로 하는 Server-Side 실행 환경

# Module
: 프로그램을 구성하는 독립적인 코드 블록 (.js 파일)

# Bundler
: 여러 모듈과 파일을 하나(혹은 여러 개)의 번들로 묶어 최적화하여 애플리케이션에서 사용할 수 있게 만들어주는 도구
- 의존성 관리, 코드 최적화, 리소스 관리 등
- Bundler가 하는 작업을 Bundling이라 함
- Vite는 Rollup이라는 Bundler를 사용하며 개발자가 별도로 기타 환경설정에 신경 쓰지 않도록 모두 설정해두고 있음

# Virtual DOM
- 가상의 DOM을 메모리에 저장하고 실제 DOM과 동기화하는 프로그래밍 개념
- 실제 DOM과의 변경 사항 비교를 통해 변경된 부분만 실제 DOM에 적용하는 방식
- 웹 애플리케이션의 성능을 향상시키기 위한 Vue의 내부 렌더링 기술
> 장점 : 효율성, 반응성, 추상화

# Scaffolding (스캐폴딩)
: 새로운 프로젝트나 모듈을 시작하기 위해 초기 구조와 기본 코드를 자동으로 생성하는 과정
```