def f(i, N, s):
    if i == N:
        print(bit, end=' ')
        print(f': {s}')
        return
    else:
        bit[i] = 1
        f(i + 1, N, s + A[i])
        bit[i] = 0
        f(i + 1, N, s)
        return


A = [1, 2, 3]
bit = [0] * 3
f(0, 3, 0)
