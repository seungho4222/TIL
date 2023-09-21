def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x < y:
        p[y] = x
    else:
        p[x] = y


V, E = map(int, input().split())
edge = []
p = list(range(V))

for _ in range(E):
    s, e, w = map(int, input().split())
    edge.append((w, s, e))  # 가중치 맨 앞으로

edge.sort()
cnt = 0
total = 0
for w, s, e in edge:
    if find_set(s) != find_set(e):
        union(s, e)
        cnt += 1
        total += w
        if cnt == E:
            break
print(f'최소신장트리 : {total}')
