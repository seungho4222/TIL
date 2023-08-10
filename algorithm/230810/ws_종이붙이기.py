# 종이접기
def origami(row):
    global memo
    if row == 1:
        return memo[1]
    elif row == 2:
        return memo[2]
    # 종이 사이즈 2개 존재, 각 종이사이즈를 뺀만큼의 경우의 수 계산후 더해주기
    elif row > 2:
        memo[row] = origami(row-1) + origami(row-2) * 2
    return memo[row]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    row = N // 10
    memo = [0] * (row+2)
    memo[1] = 1
    memo[2] = 3
    print(f'#{tc}', origami(row))