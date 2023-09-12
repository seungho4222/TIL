# 회문 판별: 문자열의 절반까지 반대값과 같은지 확인
def palindrome(x):
    for i in range(len(x) // 2):
        if x[i] != x[len(x) - i - 1]:
            return False
    return True


# 회문 찾기
def pal_check(x):
    # 가로 회문 찾기
    # 행 개수 만큼 반복
    for i in range(len(x)):
        # 행 길이 내 구하는 회문이 들어갈 수 있는 수만큼 체크
        for j in range(N - M + 1):
            # 문자열 만들기
            word_row = ''
            for k in range(M):
                word_row += arr[i][j + k]
            # 회문 판별 후 맞으면 출력
            if palindrome(word_row):
                return word_row
    # 세로 회문 찾기
    # 열 개수 만큼 반복
    for j in range(len(x)):
        # 열 길이 내 구하는 회문이 들어갈 수 있는 수만큼 체크
        for i in range(N - M + 1):
            # 문자열 만들기
            word_col = ''
            for k in range(M):
                word_col += arr[i + k][j]
            # 회문 판별 후 맞으면 출력
            if palindrome(word_col):
                return word_col


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    print(f'#{tc}', pal_check(arr))
