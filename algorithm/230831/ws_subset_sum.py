#  조합 함수
def comb(idx, visited):
    global cnt
    if idx == N:  # 원소 조합 완료
        tmp = [arr[i] for i in visited]
        if sum(tmp) == K:  # 원소의 합이 K이면 카운트
            cnt += 1
        return
    visited.append(idx)  # 해당 인덱스 포함하고 진행
    comb(idx + 1, visited)
    visited.pop()  # 해당 인덱스 포함하지 않고 진행
    comb(idx + 1, visited)


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())  # N개의 자연수, K: 부분집합의 합
    arr = list(map(int, input().split()))
    cnt = 0  # 출력값인 경우의 수
    comb(0, [])
    print(f'#{tc} {cnt}')
