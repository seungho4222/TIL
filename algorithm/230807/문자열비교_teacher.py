# 고지식한 패턴 매칭 알고리즘 사용해보기

T = int(input())
for tc in range(1, T+1):
    pattern = input()   # 내가 찾고자 하는 패턴 문자열
    text = input()  # 여기 안에서 찾고 싶다

    # 일치하는 부분이 있으면 1, 없으면 0을 출력

    # 패턴에서 비교할 문자의 위치
    pi = 0
    # 텍스트에서 비교할 문자의 위치
    ti = 0

    answer = 0  # 답

    # 비교 시작
    while ti < len(text) and pi < len(pattern):
        # 비교할 문자의 위치가 문자열의 길이보다 길면 xx

        # 현재 위치에서 비교 시작
        # 현재 위치 pi에 있는 문자와 ti에 있는 문자가 같으면
        if pattern[pi] == text[ti]:
            # pi와 ti 1씩 증가해 가면서 비교( 끝 or 다른게 나올때 까지)
            pi += 1
            ti += 1
        # 다르면? pi는 0으로 바꾸고 ti는 pi만큼 다시 앞으로 갔다가
        # 다음 위치에서 비교를 해야하니까 1 증가
        else:
            ti = ti - pi + 1
            pi = 0

        # 패턴 문자의 위치 pi가 패턴의 길이만큼 되면
        # 그전에 있던 모든 문자가 같았다는 의미 = 패턴 발견
        if pi == len(pattern):
            answer = 1
            break

    print(f'#{tc} {answer}')