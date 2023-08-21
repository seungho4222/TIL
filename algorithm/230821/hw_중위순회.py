T = 10
for tc in range(1, T+1):
    N = int(input())
    word = [0] * (N+1)
    cleft = [0] * (N+1)
    cright = [0] * (N+1)
    arr = [list(input().split()) for _ in range(N)]
    for i in arr:
        k = len(i)
        w = int(i[0])
        word[w] = int(i[1])
        if k > 2:
            cleft[w] = int(i[2])
        if k > 3:
            cright[w] = int(i[3])

    print(word)
    print(cleft)
    print(cright)


'''
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S

'''