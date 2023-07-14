import random

user = input()

print(user)

# 조건문 사용
# 누가 이겼는지 판별한후에
# 승자 출력
# 게임의 결과도 출력
# ex) 내가 가위를 내고 컴퓨터가 바위를 내서 패배하였습니다.
# ex) 내가 가위를 내고 컴퓨터가 보를 내서 승리하였습니다.

data = ["가위", "바위", "보"]
## com = 컴퓨터가 낼 가위바위보중 하나 (할때마다 바뀜)
com = random.choice(data)

print(com)

# 가위바위보 경우의 수
if user == "가위":
    if com == "가위":
        print("비겼습니다.")
    elif com == "바위":
        print("내가 {0}를 내고 컴퓨터가 {1}를 내서 패배하였습니다.".format(user, com))
    elif com == "보":
        print("야호! 이겼다. 내가 {0}를 내고 컴퓨터가 {1}를 내서 승리하였습니다.".format(user, com))

if user == "바위":
    if com == "가위":
        print("야호! 이겼다. 내가 {0}를 내고 컴퓨터가 {1}를 내서 승리하였습니다.".format(user, com))
    elif com == "바위":
        print("비겼습니다.")
    elif com == "보":
        print("내가 {0}를 내고 컴퓨터가 {1}를 내서 패배하였습니다.".format(user, com))

if user == "보":
    if com == "가위":
        print("내가 {0}를 내고 컴퓨터가 {1}를 내서 패배하였습니다.".format(user, com))
    elif com == "바위":
        print("야호! 이겼다. 내가 {0}를 내고 컴퓨터가 {1}를 내서 승리하였습니다.".format(user, com))
    elif com == "보":
        print("비겼습니다.")