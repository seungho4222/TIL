import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def get_related_artists(name):
    # 여기에 코드를 작성합니다.
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    params = {
        'q': f'{name}',
        'type': 'artist',
        'market': 'KR',
        'limit': 1
    }

    response = requests.get(f'{URL}/search', headers=headers, params=params).json()

    # 해당 가수가 있을 경우에 반환, response에 다른가수명 뜰 수 있으므로 착오 방지
    if response.get('artists').get('items')[0]['name'] == name:
        pass
    else:
        return None

    # 해당 가수의 id값 추출
    id = response.get('artists').get('items')[0]['id']

    # 연관 아티스트 기준으로 검색 / API문서 참조
    id_response = requests.get(f'{URL}/artists/{id}/related-artists', headers=headers).json()

    # 연관 아티스트 정보의 name만 추출
    related_artsts = [i['name'] for i in id_response.get('artists')]

    return related_artsts

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    아티스트가 존재하면 해당 아티스트의 id를 기반으로 연관 아티스트 목록 구성
    아티스트가 없을 경우 None을 반환
    (주의) 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(get_related_artists('NewJeans'))
    # ['STAYC', 'NMIXX', 'LE SSERAFIM', 'IVE', ... 생략 ..., 'CHUNG HA']

    pprint(get_related_artists('OldShirts'))
    # None
