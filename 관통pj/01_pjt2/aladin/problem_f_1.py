import json
import os

def best_new_books(books):
    books_2023_rank_1 = ""
    rank_1 = 0
    for filename in os.listdir('data/books'):       # 폴더 내 파일명 읽어들이기
        book_json = open(('data/books/' + filename), encoding='utf-8')
        book_js = json.load(book_json)

        if book_js['pubDate'][:4] == "2023":        # 2023년 출판된 경우
            if book_js["customerReviewRank"] > rank_1:      # 리뷰평점 비교
                rank_1 = book_js["customerReviewRank"]      # 리뷰평점 최고점 저장
                books_2023_rank_1 = book_js['title']        # 최고점이면 책이름 저장

    return books_2023_rank_1
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)
    
    print(best_new_books(books_list))
