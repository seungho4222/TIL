# C. 작가의 특정 조건에 맞는 도서 조회 2
import requests
from pprint import pprint


def bestseller_book():
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

    best_5 = [i['title'] for i in sorted(response['item'], key=lambda x:x['salesPoint'], reverse=True)[:5]]
    
    return best_5



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(bestseller_book())

