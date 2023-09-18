A = [69, 10, 30, 2, 16, 8, 31, 22]


def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))
    return result


def mergeSort(lst):
    m = len(lst)

    # 종료 조건
    if m == 1:
        return lst

    # 분할
    mid = m // 2
    left = lst[:mid]
    right = lst[mid:]

    # 정복
    left = mergeSort(left)  # 왼쪽 정렬
    right = mergeSort(right)  # 오른쪽 정렬
    return merge(left, right)


print(mergeSort(A))
