a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[i][j], end='')
print()
for j in range(len(a[0])):
    for i in range(len(a)):
        print(a[i][j], end='')
print()
for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[i][j + (len(a[0]) - 1 - 2 * j) * (i % 2)], end='')
        # 짝수행에서는 순차적으로, 홀수행은 역순으로
print()
for j in range(len(a[0])):
    for i in range(len(a)):
        print(a[i + (len(a[0]) - 1 - 2 * i) * (j % 2)][j], end='')
        # 짝수열에서는 순차적으로, 홀수열은 역순으로
print()
for i in range(3):
    # for j in range(i+1, 3):
    for j in range(3):
        if i < j:
            a[i][j], a[j][i] = a[j][i], a[i][j]
print(a)
