a = [-1, 1, -2, 3, 4, 5, 6, 7, 8, 9]

count = 0

for i in range(1 << len(a)):
    subset = [a[j] for j in range(len(a)) if i & (1 << j)]
    sum_subset = 0
    for k in subset:
        sum_subset += k
    if subset != [] and sum_subset == 0:
        count += 1

print(count)

T = int(input())
for tc in range(1, T+1):
    ...