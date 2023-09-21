def find_set(x):
    if p[x] == x:
        return x

    p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x < y:
        p[y] = x
    else:
        p[x] = y


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 섬 개수
    x_p = list(map(int, input().split()))  # x좌표
    y_p = list(map(int, input().split()))  # y 좌표
    E = float(input())  # 환경부담금 계수
    edge = []
    for i in range(N):
        dist = float('inf')
        for j in range(N):
            if i != j:
                calc = (abs(x_p[i] - x_p[j]) ** 2 + abs(y_p[i] - y_p[j]) ** 2) * E  # 환경부담금 계산
                if dist > calc:
                    dist = calc
                    edge.append([calc, i, j])
    edge.sort()
    p = list(range(N))

    cnt = 0
    total = 0
    for d, r, c in edge:
        if find_set(r) != find_set(c):
            union(r, c)
            cnt += 1
            total += d
            if cnt == N - 1:
                break
    print(f'#{tc} {int(total)}')
