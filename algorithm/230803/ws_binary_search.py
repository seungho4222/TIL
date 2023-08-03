def binary_search(page, search):
    l, r = 1, page
    count = 0
    while l <= r:
        middle = (l + r) // 2
        count += 1
        if middle == search:
            return count
        elif middle < search:
            l = middle
        else:
            r = middle


T = int(input())
for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    if binary_search(P, Pa) < binary_search(P, Pb):
        print(f'#{tc}', 'A')
    elif binary_search(P, Pa) > binary_search(P, Pb):
        print(f'#{tc}', 'B')
    else:
        print(f'#{tc}', 0)
