import json
from pprint import pprint

new_dicts = []      # 새로운 딕셔너리 취합
def books_info(books, categories):
    for book in books:
        new_dict = {}       # 새로운 딕셔너리 생성 후 필요한 정보만 추출

        new_dict['author'] = book['author']
        new_dict['categoryName'] = [name['name'] for cate_id in book['categoryId'] for name in categories if cate_id == name['id']]
        new_dict['cover'] = book['cover']
        new_dict['description'] = book['description']
        new_dict['id'] = book['id']
        new_dict['priceSales'] = book['priceSales']
        new_dict['title'] = book['title']
        new_dicts.append(new_dict)

    return new_dicts


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))