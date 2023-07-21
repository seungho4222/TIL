import json
from pprint import pprint


def artist_info(artist):
    jimin = {'genres_ids': artist['genres_ids'],
             'id': artist['id'],
             'images': artist['images'],
             'name': artist['name'],
             'type': artist['type']
             }
    # del artist['external_urls']       # del로 삭제시 return값 artist
    # del artist['uri']

    return jimin


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)
    
    pprint(artist_info(artist_dict))
