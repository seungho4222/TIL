# 0 ~ 9
# make set
parent = [i for i in range(10)]


# find set
def find_set(x):
    if parent[x] == x:
        return x
    # return find_set(parent[x])

    # 경로 압축축
    parent[x] = find_set(parent[x])
    return parent[x]


# union
def union(x, y):
    # 1. 이미 같은 집합인지 체크
    x = find_set(x)
    y = find_set(y)

    # 대표자 같으면 같은 집합
    if x == y:
        print('싸이클 발생')
        return
    # 2. 다른 집합이면, 같은 대표자로 수정
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


union(0, 1)
union(2, 3)
union(1, 3)

# 대표자 검색
print(find_set(2))
print(find_set(3))

# 같은 그룹인지 판별
t_x = 0
t_y = 2

