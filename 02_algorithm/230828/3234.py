# 팩토리얼: N-1의 최대값까지 => 8
factorial = [1] * 9
for x in range(1, 9):
    factorial[x] = x * factorial[x-1]

# 양팔저울(사용한 추 개수, 왼쪽무게, 오른쪽무게, 사용한 추 인덱스)
def scale(idx, left, right, used):
    global cnt
    # 추 전부 사용한 경우 카운트 + 1
    if idx == N:
        cnt += 1
        return
    # 남은 추로 왼쪽, 오른쪽 재 볼 필요 없는 경우
    if left > sum_w//2:  # 왼쪽이 무게 총합의 절반을 넘음 => 남은 추 다 오른쪽에 올려도 왼쪽이 큼
        n = N - idx  # 남은 추 개수
        cnt += (2**n) * factorial[n]  # 남은 추로 만들 수 있는 경우의 수 카운트 +
        return
    # 재봐야 할 경우 => 왼쪽, 오른쪽 각각 올려보기
    for i in range(N):
        if not used[i]:  # 사용 안했다면
            used[i] = 1  # 사용 기록
            scale(idx+1, left + weight[i], right, used)  # 왼쪽 추가
            if left >= right + weight[i]:  # 왼쪽이 큰 경우만
                scale(idx+1, left, right + weight[i], used)  # 오른쪽 추가
            used[i] = 0  # 기록 삭제


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 추 개수
    weight = list(map(int, input().split()))  # 추 정보
    sum_w = sum(weight)  # 추 무게 총합
    cnt = 0  # 추 올리는 방법 수
    scale(0, 0, 0, [0]*9)
    print(f'#{tc} {cnt}')


'''
# 비트마스크 사용
def dfs(left, right, bitmask):
    if (left, right, bitmask) in memo.keys():
        return memo[(left, right, bitmask)]
 
    if bitmask == (1 << n) - 1:
        return 1 
  
    cnt = 0
    for i in range(n):
        if bitmask & (1 << i):
            continue
        cnt += dfs(left + a[i], right, bitmask | (1 << i))
        if right + a[i] <= left:
            cnt += dfs(left, right + a[i], bitmask | (1 << i))
  
    memo[(left, right, bitmask)] = cnt
    return cnt
  
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = tuple(map(int, input().split()))
  
    memo = dict()
    res = dfs(0, 0, 0)
  
    print(f"#{tc} {res}")
'''