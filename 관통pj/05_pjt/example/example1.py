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


    # 보기 좋은 떡이 먹기도 좋다 !
    # print(soup.prettify())

    # 파일로 저장하기
    # with open('soup.txt', 'w', encoding="utf-8") as file:
    #     file.write(soup.prettify())


    # div 태그 중 id가 result-stats 인 요소 검색
    result_stats = soup.select_one("div#result-stats")
    print(result_stats)


# 키워드 설정
keyword = "파이썬"
get_google_data(keyword)