import json
import os

def dec_artists(artists):
    followers_list = []
    for file in os.listdir('data/artists'):     # 폴더 내 파일 순회
        artist_file = open('data/artists/' + file, encoding='utf-8')
        artist_json = json.load(artist_file)

        if artist_json['followers']['total'] > 10000000:        # 팔로워수 천만 이상
            followers_artist = {'name': artist_json['name'], 'uri-id': artist_json['uri'].split(":")[2]}    # uri 문자열중 필요한 값만 저장
            followers_list.append(followers_artist)

    return followers_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    print(dec_artists(artists_list))
