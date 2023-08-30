T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 식재료 수
    sy = [list(map(int, input().split())) for _ in range(N)]  # 시너지 정보
    min_v = 1e9  # 출력값인 A음식, B음식 시너지 차이의 최솟값
    for i in range(1, 1 << (N - 1)):  # 공집합 제외, 중복 제거를 위해 범위는 절반
        a = []  # A음식 식재료
        b = []  # B음식 식재료
        for j in range(N):  # 재료 나누기
            if i & (1 << j): a.append(j)
            else: b.append(j)
        if len(a) == len(b) == N // 2:  # 식재료 동등하게 나눈 경우
            a_sy = 0  # A음식 시너지 합
            for r in a:
                for c in a:
                    if r != c: a_sy += sy[r][c]
            b_sy = 0  # B음식 시너지 합
            for r in b:
                for c in b:
                    if r != c: b_sy += sy[r][c]
            min_v = min(min_v, abs(a_sy-b_sy))  # 시너지 차이 최소값 비교
    print(f'#{tc} {min_v}')


'''
1
4
0 5 3 8
4 0 4 1
2 5 0 3
7 2 3 0

#1 2
#2 1
#3 38
#4 15
#5 4
#6 0
#7 51
#8 23
#9 13
#10 11
'''
