def f1(b, e):
    global cnt1
    if b == 0:
        return 1
    r = 1
    for i in range(e):
        cnt1 += 1
        r *= b
    return r


def f2(b, e):
    global cnt2
    if b == 0 or e == 0:
        return 1
    if e % 2:
        r = f2(b, (e - 1) // 2)
        cnt2 += 1
        return r * r * b
    else:
        r = f2(b, e // 2)
        cnt2 += 1
        return r * r


cnt1 = 0
cnt2 = 0
print(f1(2, 10), cnt1)
print(f2(2, 10), cnt2)
