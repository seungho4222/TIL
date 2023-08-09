# def partition(A, l, r):
#     if len(A) == 1:
#         return
#     x = A[r]
#     i = l - 1
#     for j in range(l, r):
#         if A[j] <= x:
#             i += 1
#             A[i], A[j] = A[j], A[i]
#     A[i + 1], A[r] = A[r], A[i + 1]
#     return i + 1


# A = [3, 2, 4, 6, 9, 1, 8, 7, 5]
# l = 0
# r = len(A) - 1

# print(partition(A, l, r))
# print(A)
print('======================================================================')


def lomuto(arr, lo, hi):
    def partition():
        pivot = arr[hi]
        left = lo
        for right in range(lo, hi):
            if arr[right] < pivot:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
        arr[left], arr[hi] = arr[hi], arr[left]
        return left

    if lo < hi:
        pivot = partition()
        lomuto(arr, lo, pivot - 1)
        lomuto(arr, pivot + 1, hi)
    return arr


a = [3, 1, 2, 5, 4, 6]
b = [6, 5, 4, 3, 2, 1]
c = [5, 5, 3, 3, 1, 1]
print(f'lomuto a:{lomuto(a, 0, len(a) - 1)}, b:{lomuto(b, 0, len(b) - 1)}, c:{lomuto(c, 0, len(c) - 1)}')


print('======================================================================')


def hoare(arr, l, r):
    def partition():
        pivot = arr[l]
        i = l + 1
        j = r
        while i <= j:
            while(i<=j and arr[i]<=pivot) : i += 1
            while(i<=j and arr[j]>=pivot) : j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[l], arr[j] = arr[j], arr[l]
        return j

    if l < r:
        pivot = partition()
        hoare(arr, l, pivot - 1)
        hoare(arr, pivot + 1, r)
    return arr


a = [3, 1, 2, 5, 4, 6]
print(f'hoare a:{hoare(a, 0, len(a) - 1)}')