arr = [10, 6, 4, 5, 1, 3, 2, 9, 7, 8]
# 최소 힙
heap = [0] * 11
# 마지막에 넣은 원소 위치를 비교할 변수
last = 0


# 삽입 연산
def enq(item):
    global last
    last += 1
    heap[last] = item
    c = last
    p = c // 2
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


# 삭제 연산
def deq():
    global last
    temp = heap[1]
    heap[1] = heap[last]
    last -= 1
    p = 1
    c = p * 2
    while c <= last:
        if c + 1 <= last and heap[c] > heap[c+1]:
            c += 1
        if heap[p] > heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p * 2
        else:
            break
    return temp


for i in range(10):
    enq(arr[i])

print(heap)

sorted_arr = []
for i in range(10):
    sorted_arr.append(deq())

print(sorted_arr)