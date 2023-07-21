import json


def sorted_cs_books_by_price(books, categories):
    category_computer = []
    for book in books:
        new_dict = {}       # 새로운 딕셔너리 생성 후 필요한 정보만 추출

        for cate_id in book['categoryId']:
            if cate_id == 2721:     # 카테고리 컴퓨터공학만 추출
                new_dict['판매가격'] = int(book['priceSales'])
                new_dict['title'] = book['title']
                category_computer.append(new_dict)
    
    sorted(category_computer, key=lambda x:x['판매가격'], reverse=True)     # 판매가격순 정렬

    return [c_computer['title'] for c_computer in category_computer]        # 딕셔너리 내 타이틀만 추출


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    print(sorted_cs_books_by_price(books, categories_list))
