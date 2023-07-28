import requests
from pprint import pprint


def ebook_list(title):
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
        a = response['item'][0]
    except IndexError:
        return None
    a_price = a['priceSales']
    isbn = a['isbn13']

    u = f'http://www.aladin.co.kr/ttb/api/ItemLookUp.aspx?ttbkey={ttbkey}&itemIdType=ISBN13&ItemId={isbn}&output=JS&Version=20131101&OptResult=ebookList'
    res = requests.get(u).json()  # a의 isbn정보로 조회한 ebook

    ebook = res['item'][0]['subInfo']['ebookList'][0]
    ebook_info = {'isbn': ebook['isbn'], 'itemId': ebook['itemId'], 'link': ebook['link'], 'priceSales': ebook['priceSales']}
    
    # 타이틀로 조회한 ebook 목록
    qqq = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&Query={query}&QueryType={query_type}&MaxResults={max_results}&start={start}&SearchTarget=eBook&output={output}&Version={version}"
    xxx = requests.get(qqq).json()
    
    ccc = [i for i in xxx['item'] if (float(a_price) * 0.9) > int(i['priceSales'])]

    new_dict = []
    for i in ccc:
        k = {'isbn': i['isbn'], 'itemId': i['itemId'], 'link': i['link'], 'priceSales': i['priceSales']}
        new_dict.append(k)

    return ebook_info



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(ebook_list('베니스의 상인'))

    pprint(ebook_list('*'))
