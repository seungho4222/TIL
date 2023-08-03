import sys

sys.stdin = open('in.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_catch = 0
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            catch = 0
            for pr in arr[r:M + r]:
                for pc in pr[c:M + c]:
                    catch += pc
            if max_catch < catch:
                max_catch = catch
    print(f'#{tc}', max_catch)