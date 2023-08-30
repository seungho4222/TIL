# 방문구역, 누적 배터리 소비량, 방문기록
def cart(idx, total, visited):
    global min_v
    if len(visited) == N-1:  # N-1개 방문했으면 관리구역으로 돌아가고 값 비교
        total += arr[idx][0]
        min_v = min(min_v, total)
        total -= arr[idx][0]
        return
    for i in range(1, N):
        if i not in visited:  # 방문 안했으면 방문 후 재귀
            visited.append(i)
            cart(i, total + arr[idx][i], visited)
            visited.pop()
    return min_v

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 1e9
    print(f'#{tc} {cart(0,0,[])}')
