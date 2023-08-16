def f(i, N):
    if i == N:
        return
    else:
        B[i] = A[i]
        f(i + 1, N)
        return


N = 3
A = [1, 2, 3]
B = [0] * N
f(0, N)
print(B)
