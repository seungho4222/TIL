import json
from pprint import pprint


def book_info(book, categories):
    new_dict = {}       # 새로운 딕셔너리 생성 후 필요한 정보만 추출

    new_dict['author'] = book['author']
    # book의 카테고리id를 제이슨파일과 비교하여 일치할 경우 name 밸류 추출
    new_dict['categoryName'] = [name['name'] for cate_id in book['categoryId'] for name in categories if cate_id == name['id']]
    new_dict['cover'] = book['cover']
    new_dict['description'] = book['description']
    new_dict['id'] = book['id']
    new_dict['priceSales'] = book['priceSales']
    new_dict['title'] = book['title']
    
    return new_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
