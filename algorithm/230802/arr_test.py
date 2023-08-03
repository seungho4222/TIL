N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
total_1 = 0
total_2 = 0
for i in range(N):
    total_1 += arr[i][i]        # 대각선만 구하기
for i in range(N):
    total_2 += arr[i][N-1-i]    # 역대각선만 구하기

print(total_1)
print(total_2)
