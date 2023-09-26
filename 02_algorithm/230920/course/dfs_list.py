# 인접리스트 (adjacency list)
# 주의사항
# - 각 노드마다 갈 수 있는 지점의 개수가 다르다
#   -> range 쓸 때 index 조심
# 메모리가 인접 행렬에 비해 효율적
graph = [
    [1, 3],
    [0, 2, 3, 4],
    [1],
    [0, 1, 4],
    [1, 3]
]