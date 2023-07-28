# D. 작품을 쓴 작가의 다른 작품 조회
import requests
from pprint import pprint


def author_other_works(title):
    ttbkey = 'ttbkials11548001'
    query = title
    query_type = 'Title'
    max_results = 5
    start = 1
    search_target = 'Book'
    output = 'js'
    version = 20131101

    url = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&Query={query}&QueryType={query_type}&MaxResults={max_results}&start={start}&SearchTarget={search_target}&output={output}&Version={version}"
    response = requests.get(url).json()

    try:
        author_1 = response['item'][0]['author']
        author_2 = author_1.split('(')
    except IndexError:
        return None

    u = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&Query={author_2[0].strip()}&QueryType=Author&MaxResults={max_results}&start={start}&SearchTarget={search_target}&output={output}&Version={version}"
    res = requests.get(u).json()

    result = [i['title'] for i in res['item']]

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(author_other_works('베니스의 상인'))

    pprint(author_other_works('개미'))

    pprint(author_other_works('*'))
# 