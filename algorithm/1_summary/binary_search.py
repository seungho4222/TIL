def binary_search(lst, key):
    l = 0
    r = len(lst) - 1
    cnt = 0
    while l <= r:
        m = (l + r) // 2
        cnt += 1
        if lst[m] == key:
            return f'idx = {m}, cnt = {cnt}'
        elif lst[m] > key:
            r = m - 1
        elif lst[m] < key:
            l = m + 1

print(binary_search([1,3,5,6,7,9,10], 7))