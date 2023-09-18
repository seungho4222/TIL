# 이진 검색 - 재귀

arr = [2, 4, 7, 9, 11, 19, 23]


def binarysearch(low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if target == arr[mid]:
        return mid
    elif arr[mid] < target:
        return binarysearch(mid + 1, high, target)
    elif arr[mid] > target:
        return binarysearch(low, high - 1, target)


print(f'target_index : {binarysearch(0, len(arr) - 1, 7)}')
