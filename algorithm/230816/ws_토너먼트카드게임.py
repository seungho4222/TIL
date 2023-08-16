# 그룹 나누고 가위바위보
def tournament(i, j):
    # 각 그룹을 한명이 될때까지 나누기
    if i == j:
        return i
    p1 = tournament(i,(i+j)//2)
    p2 = tournament((i+j)//2+1,j)
    # 각 그룹이 한명이면 가위바위보 진행
    return game(p1, p2)

# 가위바위보 진행, 비기면 번호 작은사람 승리
def game(p1, p2):
    if card[p1] == card[p2]:
        return p1
    elif card[p1] == 1:
        if card[p2] == 2: return p2
        else: return p1
    elif card[p1] == 2:
        if card[p2] == 1: return p1
        else: return p2
    elif card[p1] == 3:
        if card[p2] == 1: return p2
        else: return p1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 1: 가위, 2: 바위, 3: 보
    # 학생 번호는 1번부터이므로 0인덱스 추가
    card = [0] + list(map(int, input().split()))
    print(f'#{tc} {tournament(1, N)}')


'''
3
4
1 3 2 1
6
2 1 1 2 3 3
7
1 3 3 3 1 1 3

'''