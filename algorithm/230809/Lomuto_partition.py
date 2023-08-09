def partition(A, l, r):
    if len(A) == 1:
        return
    x = A[r]
    i = l - 1
    for j in range(l, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


A = [3, 2, 4, 6, 9, 1, 8, 7, 5]
l = 0
r = len(A) - 1

print(partition(A, l, r))
print(A)
print('======================================================================')


def quick(arr, lo, hi):
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
        quick(arr, lo, pivot - 1)
        quick(arr, pivot + 1, hi)
    return arr


a = [3, 1, 2, 5, 4, 6]
b = [6, 5, 4, 3, 2, 1]
c = [5, 5, 3, 3, 1, 1]
print(f'quick a:{quick(a, 0, len(a) - 1)}, b:{quick(b, 0, len(b) - 1)}, c:{quick(c, 0, len(c) - 1)}')
