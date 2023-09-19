arr = [i for i in range(1, 4)]
path = [0] * 3


def backtracking(cnt):
    if cnt == 3:
        print(*path)
        return

    for num in arr:
        if num in path:
            continue
        path[cnt] = num
        backtracking(cnt + 1)
        path[cnt] = 0


backtracking(0)
