import json
from pprint import pprint


def artist_info(artist, genres):
    jimin = {}
    # 이중 for문으로 장르번호 확인후 같은 경우 장르명 반환
    jimin['genres_names'] = [genre['name'] for ids in artist['genres_ids'] for genre in genres if ids == genre['id']]
    jimin['id'] = artist['id']
    jimin['images'] = artist['images']
    jimin['name'] = artist['name']
    jimin['type'] = artist['type']
        
    return jimin


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artist_dict, genres_list))
