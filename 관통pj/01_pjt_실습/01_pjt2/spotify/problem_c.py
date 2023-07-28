import json
from pprint import pprint


def artist_info(artists, genres):
    artists_ifo = []

    for artist in artists:
        info = {}
        info['genres_names'] = [genre['name'] for ids in artist['genres_ids'] for genre in genres if ids == genre['id']]
        info['id'] = artist['id']
        info['images'] = artist['images']
        info['name'] = artist['name']
        info['type'] = artist['type']
        artists_ifo.append(info)

    return artists_ifo


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artists_list, genres_list))
