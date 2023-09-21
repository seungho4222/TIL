from collections import deque
# 8방향 델타 탐색
d = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]  # 지뢰찾기
    visited = deque()  # 방문 기록
    tmp = deque()  # 주변에 지뢰있는 좌표 저장
    cnt = 0  # 클릭 수
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '.':  # 연쇄한 적 없는 땅만 조사
                q = deque()  # bfs 탐색
                q.append([i, j])
                popping = False  # 연쇄 초기값 설정
                while q:
                    for _ in range(len(q)):
                        save = deque()  # bfs 탐색 결과 저장용
                        r, c = q.popleft()
                        mine = 0  # arr[r][c] 주변의 지뢰 개수
                        for dr, dc in d:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 0:  # 범위 내이고, 연쇄한적 없다면
                                if arr[nr][nc] == '.':  # 땅이면 좌표 저장
                                    save.append([nr, nc])
                                elif arr[nr][nc] == '*':  # 지뢰면 카운트
                                    mine += 1
                        if mine:  # 지뢰가 있다 !!
                            if arr[r][c] != 0 and [r, c] not in tmp:  # 연쇄한적 없다면 (중복 제거)
                                tmp.append([r, c])  # '주변에 지뢰가 있다면 연쇄없이 해당칸만 클릭하는 좌표' 따로 저장
                        else:  # 지뢰가 없다 !!
                            q.extend(save)  # bfs 추가 탐색
                            save.append([r, c])  # 탐색 시작 좌표도 연쇄 및 방문기록 해야하므로
                            for x, y in save:
                                arr[x][y] = 0  # 연쇄 표시
                                visited.append([x, y])  # 방문 표시 -> 연쇄한 좌표는 탐색 필요 X
                            popping = True
                if popping:  # 연쇄 성공했다면 카운트 + 1
                    cnt += 1
                # for z in range(N):
                #     print(*arr[z])
                # print()
    for x, y in tmp:
        if arr[x][y] == '.':  # 연쇄한적 없다면
            cnt += 1  # 해당칸만 클릭
    print(f'#{tc} {cnt}')


'''
델타 방향 모두 0이면 bfs 탐색 추가
연쇄 파핑 이후 남은 '.' 개수 카운트
'''

'''
from collections import deque
delta = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]


def change_bfs(ni,nj): # 지뢰판이 공개된 배열로 바꾸기
    tmp = 0
    for d in delta:
        dx, dy = ni + d[0], nj + d[1]
        if 0<=dx<N and 0<=dy<N and arr[dx][dy] == '*':
            tmp += 1

    arr[ni][nj] = tmp


def count_check(nr,nc): # 0이면 들어가서 주변숫자 다 *로 바꾸기
    Q = deque()
    Q.append([nr,nc])
    arr[nr][nc] = '*'

    while Q:
        ni, nj = Q.popleft()

        for d in delta:
            dx, dy = ni + d[0], nj + d[1]
            if 0<=dx<N and 0<=dy<N:
                if arr[dx][dy] == 0:
                    arr[dx][dy] = '*'
                    Q.append([dx,dy])

                elif arr[dx][dy] != '*':
                    arr[dx][dy] = '*'


T = int(input())+1
for tc in range(1,T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '.':
                change_bfs(i,j)

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt+= 1
                count_check(i,j)

	# 남은 숫자 갯수 세기
    for i in range(N):
        for j in range(N):
            if arr[i][j] != '*':
                cnt += 1
    print(f'#{tc} {cnt}')
    
'''
