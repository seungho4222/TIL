# 이진 검색 - 반복문

arr = [2, 4, 7, 9, 11, 19, 23]

# 문제 데이터가 정렬되어 있다라는 조건이 없다면 반드시 정렬 수행

arr.sort()


def binarysearch(target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid + 1


print(binarysearch(7))
