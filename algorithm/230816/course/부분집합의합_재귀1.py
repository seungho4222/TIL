def f(i, N):
    if i == N:
        print(bit, end=' ')
        s = 0
        for j in range(N):
            if bit[j]:
                s += A[j]
                print(A[j], end=' ')
        print(f': {s}')
        return
    else:
        bit[i] = 1
        f(i + 1, N)
        bit[i] = 0
        f(i + 1, N)
        return


A = [1, 2, 3]
bit = [0] * 3
f(0, 3)
