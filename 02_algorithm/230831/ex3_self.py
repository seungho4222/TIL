arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(arr)
k = 0
cnt = 0


def comb(idx, selected):
    global cnt
    if idx == N:
        lst = [arr[i] for i in selected]
        if sum(lst) == k:
            cnt += 1
            print(lst)
        return
    selected.append(idx)
    comb(idx + 1, selected)
    selected.pop()
    comb(idx + 1, selected)


comb(0, [])
print('cnt :', cnt)
