# open 및 json 모듈 사용예시

import json

# json 파일 열기
# open(파일 이름 , 파일 열기 방식(읽기 / 쓰기) , 인코딩 방식(문자 표현 방법))
# 이 파이썬 파일을 실행할때 터미널의 작업 경로를 반드시 확인!! => 터미널의 작업 경로를 이 파이썬 파일이 있는곳으로 변경하고 실행하세요!!
# examples 폴더 오른쪽 클릭 => 통합 터미널에서 표시 하시면 해당 경로로 새 터미널이 열립니다.
book = open("./sample.json", mode="r", encoding="utf-8")
book_detail = json.load(book)

print(book_detail)
