p = [0] * 7
rank = [0] * 7


def make_set(x):
    p[x] = x
    rank[x] = 0


def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


def find_set2(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


for i in range(1, 7):
    make_set(i)

union(1, 3)
union(2, 3)
union(5, 6)
union(1, 5)
print(p)
print(find_set(1))
