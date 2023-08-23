def postorder(t):
    if node[t].isdigit():
        return float(node[t])
    else:
        # L -> 왼쪽자식 방문
        left = postorder(cleft[t])
        # R -> 오른쪽자식 방문
        right = postorder(cright[t])
        # V -> 현재노드 방문 처리
        if node[t] == '+':
            node[t] = left + right
        elif node[t] == '-':
            node[t] = left - right
        elif node[t] == '/':
            node[t] = left / right
        elif node[t] == '*':
            node[t] = left * right
        return node[t]


T = 10
for tc in range(1, T+1):
    N = int(input())
    # 인덱스를 부모노드로 하는 자식노드
    cleft = [0] * (N+1)
    cright = [0] * (N+1)
    # 변환표
    node = [0] * (N+1)
    # 정점 정보 저장
    for i in range(N):
        info = input().split()
        # 노드의 번호 (0번째 값)
        t = int(info[0])
        # 연산자 or 피연산자 (1번째 값)
        if info[1].isdigit():   # 숫자인 경우
            node[t] = info[1]
        else:   # 연산자인 경우
            node[t] = info[1]
            cleft[t] = int(info[2])
            cright[t] = int(info[3])

    print(f'#{tc} {int(postorder(1))}')


'''
5
1 - 2 3
2 - 4 5
3 10
4 88
5 65

7
1 / 2 3
2 - 4 5
3 - 6 7
4 261
5 61
6 81
7 71

#1 13
#2 20
#3 35
#4 107
#5 369
#6 76
#7 123
#8 313
#9 238
#10 2
'''