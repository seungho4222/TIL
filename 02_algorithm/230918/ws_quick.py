def partition(A, l, r):
    p = A[l]
    i, j = l, r
    while i <= j:
        while i <= j and A[i] <= p: i += 1
        while i <= j and A[j] >= p: j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j


def hoare_quick(A, l, r):
    if l < r:
        p = partition(A, l, r)
        hoare_quick(A, l, p - 1)
        hoare_quick(A, p + 1, r)
    return A


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    print(f'#{tc} {hoare_quick(A, 0, N - 1)[N // 2]}')
