def preorder(n):
    global cnt
    if n != 0:
        cnt += 1
        preorder(cleft[n])
        preorder(cright[n])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    # 부모노드 인덱스 => 왼쪽, 오른쪽 자식노드 번호
    cleft = [0] * (E+2)
    cright = [0] * (E+2)
    for i in range(E):
        p = arr[i*2]
        c = arr[i*2+1]
        if cleft[p] == 0:
            cleft[p] = c
        else:
            cright[p] = c
    # 자식노드 스택쌓으며 탐색
    cnt = 0
    preorder(N)

    # stack = [N]
    # while stack:
    #     t = stack.pop(0)
    #     cnt += 1
    #     # 자식노드 있으면 스택 추가
    #     if cleft[t]:
    #         stack.append(cleft[t])
    #     if cright[t]:
    #         stack.append(cright[t])

    print(f'#{tc}', cnt)



'''
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10

'''