import sys

sys.stdin = open('in.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 색칠 정보 값
    coloring = [list(map(int, input().split())) for _ in range(N)]
    # 빈 매트릭스 생성
    matrix = [[0]*10 for _ in range(10)]
    # 색칠 정보 순회
    for i in coloring:
        # 색칠할 행 정보
        for j in range(i[0],i[2]+1):
            # 색칠할 열 정보
            for k in range(i[1],i[3]+1):
                # 색칠하기
                matrix[j][k] += i[4]
    # 보라색 카운트
    purple = 0
    for r in range(10):
        for c in range(10):
            # 3이면 보라색, 카운트 +1
            if matrix[r][c] == 3:
                purple += 1
    print(f'#{tc}', purple)
