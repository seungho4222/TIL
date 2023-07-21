import json
import os


def max_revenue(artists):
    popularity = 0
    popularity_artist = ''
    
    for file in os.listdir('data/artists'):     # 폴더 내 파일 순회
        artist_file = open('data/artists/' + file, encoding='utf-8')
        artist_json = json.load(artist_file)       # 순회한 json 파일 열기

        if artist_json['popularity'] > popularity:      # 인기도 비교하며 가장 높은 값과 가수 저장
            popularity = artist_json['popularity']
            popularity_artist = artist_json['name']

    return popularity_artist


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    print(max_revenue(artists_list))
