"""
    장르에 acoustic이 포함된 아티스트 이름 목록 출력하기
"""

import json
from pprint import pprint


def acoustic_artists():
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)
    
    # 장르에 acoustic이 포함된 가수만 추출
    acoustic_artists_list = [artist['name'] for artist in artists_list for id in artist['genres_ids'] if id == 339]
    # for artist in artists_list:               # 가독성 비교용
    #     for id in artist['genres_ids']:
    #         if id == 339:
    #             acoustic_artists_list.append(artist['name'])

    return acoustic_artists_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(acoustic_artists())
