# M-coloring 알고리즘
def graphColoring(graph, k, V):  # 노드정보, 색상 수, 노드 수
    colors = [0] * V  # 노드 별 색상

    def coloring(colors, i):  # i: 노드 인덱스
        if i == V:  # 색을 모두 칠하는데 성공했으면 True
            return True
        for c in range(1, k + 1):  # 색상 수만큼 색깔 칠해보기
            flag = True  # 기본값 True
            for j in range(1, V):  # 노드 순회하면서
                if j in graph[i] and colors[j] == c:  # 인접노드 색이 c면
                    flag = False  # False 변경
            if flag == True:  # 인접노드에 색상 c가 없었다!
                colors[i] = c  # 해당 인덱스에 c 색칠하기
                if coloring(colors, i + 1) == True:  # 다음 인덱스 색칠하기
                    return True  # 색칠성공했다면 True!
                colors[i] = 0  # 색상 초기화 후 다른 색도 찾아보기

    if coloring(colors, 1) == None:  # 색상 칠하는데 실패했다면
        return False  # False 반환
    return True  # 성공했다면 True 반환


# T = int(input())
# for tc in range(1, T + 1):
#     # N: 노드 수, E: 간선 수, M: 색상 수
#     N, E, M = map(int, input().split())
#     node = [[] for _ in range(N + 1)]
#     for i in range(E):
#         s, e = map(int, input().split())
#         node[s].append(e)
#         node[e].append(s)
#     result = 0  # 색칠 성공: 1, 실패: 0
#     if graphColoring(node, M, N + 1):  # 성공했다면 출력값 변경
#         result = 1
#     print(f'#{tc} {result}')
