# A. 작가의 작품 조회
import requests


def author_works(): 
    ttbkey = 'ttbkials11548001'
    query = '파울로 코엘료'
    query_type = 'Author'
    max_results = 20
    start = 1
    search_target = 'Book'
    output = 'js'
    version = 20131101

    url = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&Query={query}&QueryType={query_type}&MaxResults={max_results}&start={start}&SearchTarget={search_target}&output={output}&Version={version}"

    response = requests.get(url).json()
    
    books = [book['title'] for book in response['item']]

    return books



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    print(author_works())

    