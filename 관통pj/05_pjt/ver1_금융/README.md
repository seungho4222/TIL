#### 프로젝트 :rabbit:
1. base
    - 모든 페이지로 이동 가능한 하이퍼링크 상속

2. keyword
    - 폼을 사용하여 키워드를 생성 후, 목록 및 삭제버튼 출력

3. crawling
    - 새로운 라이브러리를 사용하여 외부사이트로부터 정보를 가져옮
    - 정보는 beautifulsoap의 메소드 사용
    - 정보에서 text만 출력한 후 text 내 숫자만 따로 저장 후 반환

4. histogram
    - 전체기간 검색 결과를 막대그래프로 출력
    - matplotlib 및 numpy를 사용하여 그래프 이미지 수정

5. advanced
    - '지난 1년'을 기준으로 필터링한 경우, 변경되는 url 참조 주소 확인
    - 크롤링하는 url 주소 변경 후 3번 과정 반복
    - trend 테이블의 search_period 값이 'year'인 필드만 필터링 한 후 4번의 막대그래프 과정 반복


#### 느낀점
