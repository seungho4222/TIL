# B. 작가의 특정 조건에 맞는 도서 조회 1
import requests
from pprint import pprint


def best_review_books():
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

    rank_9 = [book for book in response['item'] if book['customerReviewRank'] >= 9]

    return rank_9



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(best_review_books())
