# :purple_heart: *git 사용법*

**:heavy_check_mark: git 관리영역**
###### Working Directory -> Staging Area -> Repositoty
---
**로컬 저장소**
1. 로컬 저장소로 지정할 폴더 생성
2. git init 로컬 저장소 지정
    - touch 파일 생성(.확장자)
    - mkdir 폴더 생성
    - git 관리폴더 내 중복 git 설정:x:
3. git add "파일 및 폴더명 or .(전체)"
4. git commit -m "커밋 명"

**원격 저장소(github)**
1. Repository 생성
    - Initialize 체크 X
2. git remote add 깃명 주소
3. git push 깃명 master

**clone**
1. 폴더 생성
2. git clone 주소
3. git pull

---

**push에서 제외할 자료**
1. .gitignore 파일 생성
2. 제외할 파일명 입력
    - 이미 커밋한 파일 제외불가
- gitignore 설정 서비스
[gitignore](https://www.toptal.com/developers/gitignore)

**추가사항**
1. 업데이트 파일 ***git add, commit, push*** 순서
2. 새 폴더에 클론 생성시 하위폴더로 생성되니 디렉토리 확인 필수
    - cd git폴더명 : 디렉토리 변경
3. git 코드
    - git remote -v : 원격저장소 확인
    - git status : 커밋 자료 확인
    - git log : 커밋 이력 확인
    - git remote rm 깃명 : 원격저장소 삭제
---
# :+1: *마크다운 문법*

- '#*N' 글자크케

- '1.' 순서 있는 리스트

- '-' 순서 없는 리스트

- '** **' **굵게**

- '* *' *기울기*

- '~~ ~~' ~~취소선~~

- '---' 본문 나누기

- ' ``` ' 함수텍스트 출력

- '[사이트명] (주소)' 사이트 바로가기

- ' ![안뜰시 문구] (주소)' 이미지 삽입
    - (주소)에 폴더/파일명 입력 가능
    - ex : (image/coke.jpg)

- ': :' 이모지 단축키 :joy:

- '| |' 테이블 생성(엔터 윗키)

|   ?????    |   ?????   |   ?????   |
|    :---    |  :---:    |    ---:   |
|     a      |     b     |     c     |
|     d      |     e     |     f     |

