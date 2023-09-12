a = list(map(int, input()))
N = 6
baby_jin = 0
for i in range(1, 1 << (N-1)):
    group1 = []
    group2 = []
    for j in range(N):
        if i & (1 << j):  # j번 비트가 0이 아니면
            group1.append(a[j])
        else:
            group2.append(a[j])
    check = 0
    if len(group1) == 3 and len(group2) == 3:
        group1.sort()
        group2.sort()
        if group1[0] == group1[1] == group1[2]: check += 1
        elif group1[0] == group1[1] - 1 == group1[2] - 2: check += 1
        if group2[0] == group2[1] == group2[2]: check += 1
        elif group2[0] == group2[1] - 1 == group2[2] - 2: check += 1
    if check == 2:
        baby_jin = 1
        print(group1, group2)
print(baby_jin)
