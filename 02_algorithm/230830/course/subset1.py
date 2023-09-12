a = [3, 6, 7, 1, 5, 4]
N = 6
# for i in range(1, (1 << N) - 1):
for i in range(1, 1 << (N-1)):  # 1 << (N-1) == (1 << N) // 2
    group1 = []
    group2 = []
    for j in range(N):
        if i & (1 << j):  # j번 비트가 0이 아니면
            group1.append(a[j])
        else:
            group2.append(a[j])
    print(group1, group2)
