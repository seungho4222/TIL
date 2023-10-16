def counting_sort(A,B,K):
    # A [] 입력배열(0 to K) -> data
    # B [] 정렬된 배열      -> temp
    # C [] 카운트 배열      -> counts
    C = [0] * (K+1)
    
    for i in range(0, len(A)):
        C[A[i]] += 1
    print(C)
    for i in range(1,len(C)):
        C[i] += C[i-1]
    print(C)
    for i in range(len(A)-1,-1,-1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    print(B)

A = [0,4,1,3,1,2,4,1]
B = [0] * len(A)
K = 4

counting_sort(A,B,K)