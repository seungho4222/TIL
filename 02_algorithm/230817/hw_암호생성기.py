# 한 사이클: 1부터 5씩 빼주고 뒤로 보내기
def cycle():
    global front, rear
    # 5번 반복
    for i in range(1, 6):
        front += 1
        # 앞 숫자 꺼내오기
        num = password[front]
        rear += 1
        # 숫자 빼주고 뒤로 보내기
        if num - i > 0:
            password[rear] = num - i
        # 빼준값이 0 이하면 리턴
        else:
            password[rear] = 0
            return True
    return False


T = 10
for tc in range(1, T + 1):
    _ = int(input())
    data = list(map(int, input().split()))
    # 8자리 수 * (9999에서 3(1~5)씩 뺄 경우 대략 3500번)
    password = [0] * 28000
    front = rear = -1
    # 처음에 패스워드 입력
    for i in range(len(data)):
        rear += 1
        password[i] = data[i]
    # 사이클 반복
    while True:
        if cycle():
            break

    print(f'#{tc}', end=' ')
    for i in range(rear - 7, rear + 1):
        print(password[i], end=' ')
    print()

'''
1
9550 9556 9550 9553 9558 9551 9551 9551 
2
2419 2418 2423 2415 2422 2419 2420 2415 
3
7834 7840 7840 7835 7841 7835 7835 7838 
4
4088 4087 4090 4089 4093 4085 4090 4084 
5
2945 2946 2950 2948 2942 2943 2948 2947 
6
670 667 669 671 670 670 668 671 
7
8869 8869 8873 8875 8870 8872 8871 8873 
8
1709 1707 1712 1712 1714 1710 1706 1712 
9
10239 10248 10242 10240 10242 10242 10245 10235 
10
6580 6579 6574 6580 6583 6580 6577 6581 

'''
