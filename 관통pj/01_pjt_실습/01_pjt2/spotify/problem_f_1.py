"""
    팔로워가 5,000,000이상, 10,000,000미만인 아티스트들을 
    아티스트 이름과 팔로워를 목록으로 출력하기
"""

import json
from pprint import pprint
import os


def get_popular():
    followers_list = []
    for file in os.listdir('data/artists'):
        artist_file = open('data/artists/' + file, encoding='utf-8')
        artist_json = json.load(artist_file)

        if 5000000 < artist_json['followers']['total'] < 10000000:      # 해당 범위 내 팔로워 수 해당자 추출
            followers_artist = {'followers': artist_json['followers']['total'], 'name': artist_json['name']}    
            followers_list.append(followers_artist)

    return list(sorted(followers_list, key= lambda x: x['followers'], reverse=True))


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_popular())
