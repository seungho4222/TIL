def postorder(t):
    if t:
        postorder(t * 2)
        postorder(t * 2 + 1)
        if not tree[t]:
            tree[t] = tree[t * 2] + tree[t * 2 + 1]


T = int(input())
for tc in range(1, T + 1):
    # N: 노드의 개수, M: 리프노드의 개수, L: 출력 노드 번호
    N, M, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    tree = [0] * (N + 1)
    for i in arr:
        tree[i[0]] = i[1]
    postorder(1)
    print(tree)


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
