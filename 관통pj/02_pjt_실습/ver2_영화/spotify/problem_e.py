import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def recommendation(track, artist, genre):
    # 여기에 코드를 작성합니다.
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()

    # 트랙 id 추출
    response_tr = requests.get(f'{URL}/search?q={track}&type=track&market=KR&limit=1', headers=headers).json()
    track_id = response_tr.get('tracks').get('items')[0]['id']

    # 아티스트 id 추출
    response_ar = requests.get(f'{URL}/search?q={artist}&type=artist&market=KR&limit=1', headers=headers).json()
    artist_id = response_ar.get('artists').get('items')[0]['id']

    # 추천 목록 기준으로 검색 / API문서 참조
    response_recom = requests.get(f'{URL}/recommendations?limit=5&market=KR&seed_artists={artist_id}&seed_genres={genre}&seed_tracks={track_id}' , headers=headers).json()

    # 추천트랙 name만 추출 / 추천이기에 매번 다른값 반환
    recommendation_list = [i['name'] for i in response_recom.get('tracks')]

    return recommendation_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    주어진 트랙, 아티스트 이름, 장르로 음악 트랙 추천 목록 출력하기
    (주의) 요청마다 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('HypeBoy', 'BTS', 'acoustic'))
    # ['Best Of Me', 'A Drop in the Ocean', 'We Are', 'Dear Mr. President', 'Hurt']
