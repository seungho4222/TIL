# 델타 이동
def move(x, y, cnt):
    global word
    if cnt == 7:  # 7자리 수 완료
        if word not in dup_check:  # 중복 체크 후 추가
            dup_check.append(word)
        return
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = x + di, y + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            word += str(arr[ni][nj])  # 숫자 추가
            move(ni, nj, cnt + 1)
            word = word[:cnt]  # 재귀 빠져나오면 숫자 제거


T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    # 중복 체크
    dup_check = []

    for r in range(4):
        for c in range(4):
            word = ''
            word += str(arr[r][c])  # 첫 숫자 추가 후 탐색 시작
            move(r, c, 1)
    print(f'#{tc} {len(dup_check)}')
