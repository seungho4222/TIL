import json
import os

def best_book(books):
    rank_1 = 0              # 리뷰 평점 비교용
    rank_1_book = ""        # 리뷰 평점 최고인 책 타이틀 저장
    for filename in os.listdir('data/books'):       # 폴더 내 파일명 읽어들이기
        book_json = open(('data/books/' + filename), encoding='utf-8')
        book_js = json.load(book_json)
        
        if float(book_js["customerReviewRank"]) > rank_1:
            rank_1 = float(book_js["customerReviewRank"])
            rank_1_book = book_js["title"]
    
    for check in books:
        if check["title"] == rank_1_book:
            return rank_1_book
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)
    
    print(best_book(books_list))
