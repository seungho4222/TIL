# 후위순회
def postorder(t):
    # 마지막 노드번호 이하면 진행
    if t <= N:
        postorder(t * 2)
        postorder(t * 2 + 1)
        # 해당 트리에 값이 없으면
        if not tree[t]:
            # 자식노드가 하나인 경우
            if t * 2 + 1 > N:
                tree[t] = tree[t * 2]
            # 자식노드가 두개인 경우
            else:
                tree[t] = tree[t * 2] + tree[t * 2 + 1]


T = int(input())
for tc in range(1, T + 1):
    # N: 노드의 개수, M: 리프노드의 개수, L: 출력 노드 번호
    N, M, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    # 노드번호를 인덱스로 하는 저장값
    tree = [0] * (N + 1)
    # 리프 노드 값 입력
    for i in arr:
        tree[i[0]] = i[1]
    # 후위순회 진행 및 노드번호 L 출력
    postorder(1)
    print(f'#{tc} {tree[L]}')


'''
3
5 3 2
4 1
5 2
3 3
10 5 2
8 42
9 468
10 335
6 501
7 170
17 9 4
16 479
17 359
9 963
10 465
11 706
12 146
13 282
14 828
15 962

#1 3
#2 845
#3 1801
'''
