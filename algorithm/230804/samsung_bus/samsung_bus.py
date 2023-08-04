import sys

sys.stdin = open('in.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = [0] * 5001  # 1~5000번 각 정류장
    for _ in range(N):  # N개의 노선에 대해
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            cnt[i] += 1

    P = int(input())
    bus_stop = [int(input()) for _ in range(P)]
    print(f'#{tc}', end=' ')
    for x in bus_stop:
        print(cnt[x], end=' ')
    print()