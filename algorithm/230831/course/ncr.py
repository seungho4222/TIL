def ncr(n, r):
    if r == 0:
        print(tr)
    elif n < r:
        return
    else:
        tr[r - 1] = a[n - 1]
        ncr(n - 1, r - 1)
        ncr(n - 1, r)


N = 5
R = 3
a = [1, 2, 3, 4, 5]
tr = [0] * R
ncr(N, R)
