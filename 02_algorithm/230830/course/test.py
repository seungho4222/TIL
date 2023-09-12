def f(i, N):  # i 현재상태, N 목표
    if i == N:
        print(B)
        return
    else:
        B[i] = A[i]
        f(i + 1, N)


N = 5
A = [1, 2, 3, 4, 5]
B = [0] * N
f(0, N)
