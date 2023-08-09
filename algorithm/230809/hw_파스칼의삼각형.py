def paskal(x):
    lst = [1] * x
    if x == 1:
        print(*lst)
        return
    if x == 2:
        paskal(x - 1)
        print(*lst)
        return lst

    before = paskal(x - 1)
    for i in range(1, len(lst)-1):
        lst[i] = before[i-1] + before[i]
    print(*lst)
    return lst

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    paskal(N)