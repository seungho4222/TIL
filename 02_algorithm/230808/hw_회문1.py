def palindrome(x):
    for i in range(len(x)//2):
        if x[i] != x[len(x) - i -1]:
            return False
    return True


T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(8)]

    cnt = 0
    # 가로 확인
    for i in range(8):
        for j in range(8-N+1):
            # 가로문자 만들기
            word_row = ''
            for k in range(N):
                word_row += arr[i][j+k]
            # 회문체크
            if palindrome(word_row):
                cnt += 1
    # 세로 확인
    for j in range(8):
        for i in range(8-N+1):
            #세로문자 만들기
            word_col = ''
            for k in range(N):
                word_col += arr[i+k][j]
            # 회문체크
            if palindrome(word_col):
                cnt += 1
    print(f'#{tc}', cnt)
            