# 회전 하는 기어번호에 따른 기어 확인 순서
order = {1: [[0, 1], [1, 2], [2, 3]],
         2: [[1, 0], [1, 2], [2, 3]],
         3: [[2, 3], [2, 1], [1, 0]],
         4: [[3, 2], [2, 1], [1, 0]]}

T = int(input())
for tc in range(1, T + 1):
    K = int(input())  # K: 자석 회전 횟수
    # 0번 인덱스 S(=1)면 각 1, 2, 4, 8점 획득
    gear = [list(map(int, input().split())) for _ in range(4)]
    score = 0  # 출력값인 점수 합
    for _ in range(K):  # K번 반복
        s, d = map(int, input().split())  # 회전 기준, 방향
        idx = []  # 2번과 6번인덱스 비교하기
        for i in gear:
            idx.append((i[6], i[2]))
        check = [0, 0, 0, 0]  # 기어번호를 인덱스로 하는 회전방향 (회전은 1 or -1)
        check[s-1] = d  # 회전 기준번호의 방향 입력
        for g1, g2 in order[s]:  # 순서대로 확인
            if g1 < g2:  # (1,2),(2,1)와 같이 g1, g2를 다르게 하는 이유는 체크 기준 때문
                if idx[g1][1] != idx[g2][0] and check[g1]:  # 자성이 다르고 앞 기어가 회전했으면
                    check[g2] = -check[g1]  # 뒤 기어는 반대방향으로 회전
                elif s == 1 or s == 2: break  # 뒤 순서 기어는 확인 안해도 됨
            else:  # 위와 동일! (반대방향)
                if idx[g1][0] != idx[g2][1] and check[g1]:
                    check[g2] = -check[g1]
                elif s == 3 or s == 4: break
        for j in range(4):  # 체크에 값이 있으면 방향대로 기어 회전
            if check[j] == 1:
                gear[j].insert(0, gear[j].pop())
            elif check[j] == -1:
                gear[j].append(gear[j].pop(0))
    for k in range(4):  # 회전 종료 후 기어의 상단이 S면 점수 획득
        if gear[k][0] == 1:
            score += 2 ** k
    print(f'#{tc} {score}')


'''
1
2
1 0 0 1 0 0 0 0
0 1 1 1 1 1 1 1
0 1 0 1 0 0 1 0
0 1 0 0 1 1 0 1
3 1
1 1

'''