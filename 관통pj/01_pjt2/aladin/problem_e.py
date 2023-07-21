import json
import os

def new_books(books):
    books_2023 = []
    for filename in os.listdir('data/books'):       # 폴더 내 파일명 읽어들이기
        book_json = open(('data/books/' + filename), encoding='utf-8')
        book_js = json.load(book_json)

        if book_js['pubDate'][:4] == "2023":
            books_2023.append(book_js.get('title'))
    return sorted(books_2023, reverse=True)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)
    
    print(new_books(books_list))
