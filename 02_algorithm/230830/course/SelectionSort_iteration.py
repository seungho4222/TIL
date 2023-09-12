def SelectionSort(A):
    n = len(A)
    for i in range(n - 1):
        minI = i
        for j in range(i + 1, n):
            if A[j] < A[minI]:
                minI = j
        A[minI], A[i] = A[i], A[minI]


lst = [1, 5, 9, 7, 4, 2]
SelectionSort(lst)
print(lst)
