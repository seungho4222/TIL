lst = [1, 2, 3, 4, 5]
N = 5
R = 3


def comb(idx, r, selected):
    if idx == N:
        if r == R:
            print([lst[i] for i in selected])
        return
    selected.append(idx)
    comb(idx + 1, r + 1, selected)
    selected.pop()
    comb(idx + 1, r, selected)


comb(0, 0, [])
