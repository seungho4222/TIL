def subset(i, N, s, c):
    if s == 0 and c != 0:
        return 1
    elif i == N:
        return 0
    else:
        if subset(i + 1, N, s + arr[i], c + 1):
            return 1
        if subset(i + 1, N, s, c):
            return 1
        return 0


arr = [1, 2, 3, 4, 5]
N = len(arr)
bit = [0] * N
cnt = 0
print(subset(0, N, 0, 0))
