# 중위순회
def inorder(n):
    global inorder_arr
    if n:
        inorder(cleft[n])
        inorder_arr += [n]
        inorder(cright[n])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [0] * (N + 1)
    # 부모노드 인덱스 => 왼쪽, 오른쪽 자식노드 번호
    cleft = [0] * (N + 1)
    cright = [0] * (N + 1)
    for i in range(2, N + 1):
        if cleft[i // 2] == 0:
            cleft[i // 2] = i
        else:
            cright[i // 2] = i
    # 중위순회 순서 => 해당 값이 노드 번호, 인덱스+1이 저장값
    inorder_arr = []
    inorder(1)
    # 인덱스 0번부터 이므로 + 1
    print(f'#{tc}', inorder_arr.index(1) + 1, inorder_arr.index(N // 2) + 1)
