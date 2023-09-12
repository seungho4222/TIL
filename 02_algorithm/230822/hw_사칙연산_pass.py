T = 10
for tc in range(1, T+1):
    N = int(input())
    # 정점 정보
    arr = [0] + [list(input().split()) for _ in range(N)]
    # 정점번호를 인덱스로 하는 리스트
    node = [0] * (N+1)
    # 리프노드 번호 저장
    for i in range(N,0,-1):
        # 숫자면 저장
        if arr[i][1] not in '+-/*':
            node[i] = int(arr[i][1])
        # 연산자 무시시
        else: continue
    # 정점 연산
    for i in range(N,0,-1):
        # 숫자면 무시
        if arr[i][1] not in '+-/*':
            continue
        # 연산자 계산
        else:
            num = int(arr[i][0])
            if arr[i][1] == '+':
                node[num] = node[int(arr[i][2])] + node[int((arr[i][3]))]
            elif arr[i][1] == '-':
                node[num] = node[int(arr[i][2])] - node[int((arr[i][3]))]
            elif arr[i][1] == '/':
                node[num] = node[int(arr[i][2])] / node[int((arr[i][3]))]
            elif arr[i][1] == '*':
                node[num] = node[int(arr[i][2])] * node[int((arr[i][3]))]

    print(f'#{tc} {node[1]:.0f}')