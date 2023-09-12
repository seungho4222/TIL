T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    result = ''

    for c in range(15):  # 세로열 최대 15
        for r in range(5):  # 문자 5개
            if c < len(arr[r]):
                result += arr[r][c]
    print(f'#{tc}', result)



'''
2
ABCDE
abcde
01234
FGHIJ
fghij
AABCDD
afzz
09121
a8EWg6
P5h3kx

'''