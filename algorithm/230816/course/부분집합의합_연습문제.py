def f(i, N, s, t):
    global cnt
    cnt += 1
    if s == t:
        print(bit)
        return
    elif i == N:
        return
    elif s > t:
        return
    else:
        bit[i] = 1
        f(i + 1, N, s + A[i], t)
        bit[i] = 0
        f(i + 1, N, s, t)
        return


N = 10
A = [i for i in range(1, N + 1)]
bit = [0] * N
cnt = 0
f(0, N, 0, 1)
print(cnt)
