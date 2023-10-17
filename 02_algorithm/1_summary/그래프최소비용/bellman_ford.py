N, M = map(int, input().split())  # N: 정점 수 M: 간선 수
adjl = []  # 연결 정보
D = [1e9] * (N+1)  # 이동 거리 무한 지정
D[1] = 0  # 시작위치 0
for _ in range(M):
    s, e, w = map(int, input().split())  # 시작, 도착, 가중치
    adjl.append((s, e, w))

isCycle = False  # 무한 루프 체크 값
for i in range(N):  # 모든 거리를 무한대로 설정 => N-1만큼 반복해야 모든 루트 확인 가능
    for start, end, wt in adjl:  # 연결정보 확인
        if D[start] != 1e9:  # 연결된 이전 정점이 있다면
            distance = D[start] + wt  # (1번 ~ start) + (start ~ end)
            if distance < D[end]:  # 1번 ~ end보다 작은 값이면
                if i == N-1:  # 마지막 반복문에서도 작아지는 구간이 있다면
                    isCycle = True  # 음의 무한 루프 발생
                    break
                D[end] = distance  # 최단거리 갱신

if isCycle:
    print('음의 무한 루프')
else:
    print(D)