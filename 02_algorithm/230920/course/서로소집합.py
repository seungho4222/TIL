# p[x] -> x의 부모
# p[x] == x -> x가 속한 집합의 대표가 x
# p[x] != x -> x는 x가 속한 집합의 대표가 아님
p = [0] * 7


# 1. 집합 초기화
def make_set(x):
    p[x] = x


# 2. x가 속한 집합의 대표를 얻는 연산
def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])


# 3. 두 집합을 합치는 연산
def union(x, y):
    p[find_set(y)] = find_set(x)


for i in range(1, 7):
    make_set(i)

union(1, 3)
union(2, 3)
union(5, 6)
print(p)
