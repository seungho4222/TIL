arr = [10, 6, 4, 5, 1, 3, 2, 9, 7, 8]
# 최대 힙
heap = [0] * 11
# 마지막에 넣은 원소 위치를 비교할 변수
last = 0


# 삽입 연산
def enq(item):
    global last
    last += 1
    heap[last] = item

    # 원소추가 후 (부모노드 > 자식노드) 조건 확인
    # 현재 위치를 자식노드로 보고, 부모노드 위치 계산 (2로 나누면 계산 가능)
    c = last
    p = c // 2
    # 부모노드가 존재하고, 자식노드가 부모노드보다 작을때까지 위치 변경
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        # 그 위의 부모노드도 비교
        c = p
        p = c // 2


# 삭제 연산
def deq():
    global last
    # 루트 저장
    temp = heap[1]
    # 마지막노드를 루트 위치로 변경
    heap[1] = heap[last]
    # 원소 하나 삭제했으니 마지막 원소 인덱스 -1
    last -= 1
    # 루트부터 자리를 찾아가기 시작
    p = 1
    c = p * 2   # 일단 왼쪽 자식부터 비교 (완전이진트리)

    # 자리조정 => 최대힙은 부모가 자식보다 큼
    # 부모가 자식보다 작으면 계속 자리 교환

    # 왼쪽자식의 인덱스가 last보다 작아야 트리 안에 존재 하는 것
    while c <= last:
        # 왼쪽 자식이 있으면 오른쪽 자식도 있나 확인
        # 부모 > 자식
        if c + 1 <= last and heap[c] < heap[c+1]:
            c += 1

        if heap[p] < heap[c]:
            # 자식이 더 크면 자리 교환
            heap[p], heap[c] = heap[c], heap[p]
            p = c   # 자식을 새로운 부모로 생각
            c = p * 2   # 왼쪽자식을 기준으로 비교 계속
        else:
            break
    # 루트노드 리턴
    return temp


for i in range(10):
    enq(arr[i])

print(heap)

sorted_arr = []
for i in range(10):
    sorted_arr.append(deq())

print(sorted_arr)