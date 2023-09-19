from collections import deque

d = [[0, 1], [1, 0], [-1, 0], [0, -1]]
no = [1, 2]  # 1: 코어, 2: 전선


def connect(idx, total, core_cnt):
    global result, max_cores
    if core_cnt + l - idx < max_cores:  # 남은 코어 모두 연결해도 맥스보다 작으면 리턴
        return
    if idx == l:  # 모든 코어 확인했으면 출력값 갱신
        if max_cores == core_cnt:
            result = min(result, total)
        elif max_cores < core_cnt:
            max_cores = core_cnt
            result = total
        return
    r, c = cores[idx]  # idx 번째 코어 확인
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        save = deque()  # 전선 좌표 저장
        cnt = 0  # 전선 수
        check = 0  # 연결 여부
        while True:
            if arr[nr][nc] in no:  # 코어 및 전선에 막혀 연결 못함
                break
            elif arr[nr][nc] == 0:  # 쭈욱 가보자
                save.append([nr, nc])
                cnt += 1
                nr += dr
                nc += dc
                continue
            else:
                check = 1  # 전선 연결 성공
                break
        for x, y in save:  # 전선 연결 표기
            arr[x][y] = 2
        if check == 0:  # 연결 못했으면 전선 수 초기화
            cnt = 0
        connect(idx + 1, total + cnt, core_cnt + check)
        for x, y in save:  # 전선 표기 제거
            arr[x][y] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # N*N 배열
    cores = []  # 코어 좌표
    arr = [[-1] * (N + 2)]  # 주변 전기로 둘러싸기
    for row in range(N):
        tmp = list(map(int, input().split()))
        arr.append([-1] + tmp + [-1])
        for col in range(N):  # 코어 저장
            if arr[row + 1][col + 1] == 1:
                cores.append([row + 1, col + 1])
    arr.append([-1] * (N + 2))  # 전기 !!

    l = len(cores)  # 코어 수
    result = 1e9
    max_cores = 0

    connect(0, 0, 0)
    print(f'#{tc} {result}')


'''
1
7    
0 0 1 0 0 0 0
0 0 1 0 0 0 0
0 0 0 0 0 1 0
0 0 0 0 0 0 0
1 1 0 1 0 0 0
0 1 0 0 0 0 0
0 0 0 0 0 0 0

'''
