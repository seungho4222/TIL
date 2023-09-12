# DFS - 그래프의 형태를 어떤 방법으로 나타내느냐

# 1. 인접행렬 => 2차원 배열
# 1번 정점에서 2번 정점으로 가는 길이 있다
# adj_m[1][2] = 1
# 2번 정점에서 3번 정점으로 가는 길이 없다
# adj_m[2][3] = 0

# s : 시작 정점 번호
# V : 정점의 개수
def dfs(s, V):
    visited = [0] * V
    stack = []
    # 시작 정점은 방문 처리
    visited[s] += 1
    print(node[s])
    # 현재 방문한 정점 i
    i = s

    # 모든 정점을 방문할때까지 반복
    while True:
        # 현재 정점에서 탐색할 수 있는 정점 확인
        # i에서 다른 정점 j로 갈 수 있는 길 확인
        # 인접 행렬 or 인접 리스트
        # adj_m[i][j] = 1이면 길 존재
        for j in range(V):
            # j 방문기록 확인
            if adj_m[i][j] == 1 and not visited[j]:
                # j번째 정점에서
                stack.append(i)
                # j번째 정점에서 하고싶은 일
                print(node[j])
                # 방문 처리
                visited[j] = 1
                # 현재 위치 j로 바꾸고 다음 탐색 진행
                i = j
                # 새로운 i에서 방문을 다시 시작하기 위해 break
                break
        else:
            # 내가 i에서 탐색했는데 더 이상 탐색할 정점이 없는 경우
            # 제일 최근에 방문했던 정점으로 돌아가기
            if stack:
                # stack에 원소가 있다면 돌아갈 곳 존재
                # 하나 꺼내서 돌아가기, i번 정점부터 탐색 시작
                i = stack.pop()
            else:
                # stack에 원소가 없다면, 탐색 완료, 반복 종료
                break
    return


#         A  B  C  D  E  F  G
adj_m = [[0, 1, 1, 0, 0, 0, 0],  # A
         [1, 0, 0, 1, 1, 0, 0],  # B
         [1, 0, 0, 0, 1, 0, 0],  # C
         [0, 1, 0, 0, 0, 1, 0],  # D
         [0, 1, 1, 0, 0, 1, 0],  # E
         [0, 0, 0, 1, 1, 0, 1],  # F
         [0, 0, 0, 0, 0, 1, 0]  # G
         ]
node = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
N = 7
dfs(0, N)

# 2. 인접리스트
# adj_l[i] => i번 정점과 연결되어 있는 정점의 모음(리스트)
# adj_l[A] => [B,C]
'''
7 8
1 2
1 3
2 4
2 5
3 7
4 6
5 6
6 7
'''


def dfs_1(s, V):
    visited = [0] * (V + 1)
    stack = []
    i = s
    visited[i] = 1
    print(i)

    # 모든 정점을 방문할 때까지 반복
    while True:
        # 현재 정점 i에서 갈 수 있는 정점 j 찾기
        for j in adj_l[i]:
            if visited[j] == 0:
                stack.append(i)  # 내가 왔던 정점 기억
                i = j  # 새로운 i에서 탐색 시작 하도록 바꾸기
                visited[j] = 1
                print(i)
                break
        # 현재 정점 i에서 갈 수 있는 정점이 없었다.
        else:
            # 돌아가기
            if stack:
                i = stack.pop()
            else:
                break


V, E = map(int, input().split())
adj_l = [[] for _ in range(V + 1)]
for i in range(E):
    # 연결이 되려면 연결시작점 s, 연결 종료 e
    s, e = map(int, input().split())
    # 인접 리스트
    # adj_l[s] = s 정점에서 갈 수 있는 정점들의 리스트
    adj_l[s].append(e)
    adj_l[e].append(s)

dfs_1(1, V)
