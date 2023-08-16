# 순열 계산
def perm(r, total):
    global ans
    # 모든 행의 값을 더해줬다면 값 비교
    if r == N:
        if ans > total:
            ans = total
            return
    # 중간값이 ans보다 커지면 리턴
    if total > ans:
        return
    # 열 번호 순회
    for c in range(N):
        # 선택되지 않았다면
        if c not in selected:
            # 선택 후 다음 행 진행
            selected[r] = c
            perm(r + 1, total + arr[r][c])
            # 선택 초기화
            selected[r] = -1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 결과값은 최댓값을 기준으로 비교 시작
    ans = 10 * N
    # 선택은 0, 1, 2 행을 선택하므로 -1로 초기화
    selected = [-1] * N
    perm(0, 0)
    print(f'#{tc} {ans}')


'''
3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8

'''
