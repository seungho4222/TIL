import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def get_popular_tracks():
    # 여기에 코드를 작성합니다.
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    params = {
        'q': 'genre:k-pop',
        'type': 'track',
        'market': 'KR',
        'limit': 20
    }

    response = requests.get(f'{URL}/search', headers=headers, params=params).json()

    result = response.get('tracks').get('items')

    # 음악트랙 20개중 popularity 90이상 트랙의 name만 추출
    kpop = [i['name'] for i in result if i['popularity'] >= 90]

    return kpop


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    (주의) 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(get_popular_tracks())
    """
    ['Cupid - Twin Ver.', 'Take Two', 'Like Crazy', 'MONEY', 'OMG', 'Like Crazy']
    """
