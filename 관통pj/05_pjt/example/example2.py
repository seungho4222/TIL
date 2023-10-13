from bs4 import BeautifulSoup
from selenium import webdriver


def get_google_data(keyword):
    url = f'https://www.google.com/search?q={keyword}'
    
    # 크롬이 열린다. 동적인 내용들이 채워진다
    driver = webdriver.Chrome()
    driver.get(url)

    # 열린 페이지 소스를 받아온다
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # g
    # LC201b MBeuO DKV0Md

    # 결과물 제목만 추출
    # 1. div 태그 중 g class 를 가진 모든 요소 선택
    g_list = soup.select("div.g")
    for g in g_list:
        # 요소 안에 LC201b MBeuO DKV0Md class를 가진 특정 요소
        title = g.select_one(".LC20lb.MBeuO.DKV0Md")
        if title is not None:
            print(f'제목 = {title.text}')


# 키워드 설정
keyword = "백종원"
get_google_data(keyword)


# 주소 뒤에 robots.txt 란? => Allow or Disallow