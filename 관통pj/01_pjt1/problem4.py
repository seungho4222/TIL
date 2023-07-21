import pprint
import requests

# 상품과 옵션 정보들을 담고 있는 새로운 객체를 만들어 반환하시오.
# [힌트] 상품 리스트와 옵션 리스트를 금융상품 코드를 기준으로 매칭할 수 있습니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 변수에 저장합니다.
# 3. 2번의 결과 중 key 값이 "baseList" 인 데이터를 변수에 저장합니다.
# 4. 2번의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 5. 3번에서 저장된 변수를 순회하며, 4번에서 저장된 값들에서 금융 상품 코드가 
#     같은 모든 데이터들을 가져와 새로운 딕셔너리로 저장합니다.
#     저장 시, 명세서에 맞게 출력되도록 저장합니다.
# 6. 5번에서 만든 딕셔너리를 결과 리스트에 추가합니다.


def get_deposit_products():
  # 본인의 API KEY 로 수정합니다.
    api_key = "4646023347c3b894c9d231e16a0a24e0"

  # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

  # 응답을 JSON 형태로 변환
    response = requests.get(url).json()

    key = response['result'].keys()
    baseList = response['result']['baseList']       # 상품리스트
    optionList = response['result']['optionList']   # 옵션리스트

    new_dict = []
    for base in baseList:       # 상품리스트 순회
        deposit_product = {}    # 금융상품별 딕셔너리
        deposit_info = []       # 금융상품별 금리 정보
        for option in optionList:       # 옵션리스트 순회
            option_dict = {}            # 옵션별 금리 정보
            if base['fin_prdt_cd'] == option['fin_prdt_cd'] :       # 금융상품코드 매칭
                option_dict['저축 금리'] = option['intr_rate']       # 옵션별 금리 정보 추가
                option_dict['저축 기간'] = option['save_trm']
                option_dict['저축금리유형'] = option['intr_rate_type']
                option_dict['저축금리유형명'] = option['intr_rate_type_nm']
                option_dict['최고우대금리'] = option['intr_rate2']
                deposit_info.append(option_dict)        # 옵션별 금리 정보 취합하여 금융상품별 금리 정보 생성
        deposit_product['금리정보'] = deposit_info
        deposit_product['금융상품명'] = base['fin_prdt_nm']
        deposit_product['금융회사명'] = base['kor_co_nm']
        new_dict.append(deposit_product)        # 금융상품별 딕셔너리 취합하여 새로운 리스트 생성

    return new_dict


if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)