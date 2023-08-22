# 최소 힙 - 삽입 연산
def enq(item):
    global last
    # 힙의 마지막 노드에 아이템 추가
    last += 1
    heap[last] = item
    # 부모노드 < 자식노드 되도록 정렬
    c = last
    p = c // 2
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    heap = [0] * (N+1)
    last = 0
    # nums에 있는 숫자 힙에 삽입
    for i in range(N):
        enq(nums[i])
    # 출력값: 마지막 노드의 조상 노드에 저장된 정수의 합
    ans = 0
    # now: 마지막 노드의 조상 노드 순회
    now = N // 2
    while now != 0:
        ans += heap[now]
        now //= 2
    print(f'#{tc} {ans}')


'''
3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40

#1 7
#2 5
#3 65
'''