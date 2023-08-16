def f(i, N):
    if i == N:
        print(A)
    else:
        for j in range(i, N):  # 자신부터 오른쪽끝까지
            A[i], A[j] = A[j], A[i]
            f(i + 1, N)
            A[i], A[j] = A[j], A[i]


A = [0, 1, 2]
f(0, 3)
