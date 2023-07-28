# import requests

# url = 'https://fakestoreapi.com/carts'
# response = requests.get(url)

# print(response.json())


import json     # 내장 모듈

# json 데이터
json_data = '''
{
    "name": "김싸피",
    "age": 28,
    "hobbies": [
        "공부하기",
        "복습하기"
    ]
}
'''

data = json.loads(json_data)
print(type(data))

# JSON 데이터에서 원하는 데이터만 가져오기
name = data.get('name')

print(name)