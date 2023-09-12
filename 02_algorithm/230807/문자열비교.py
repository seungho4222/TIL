T = int(input())
for tc in range(1, T+1):
    pattern = input()
    text = input()
    # 패턴과 텍스트 인덱스 번호
    pi = 0
    ti = 0
    # 패턴이 있으면 1, 없으면 0
    answer = 0
    # 패턴 및 텍스트 길이만큼 반복
    while pi < len(pattern) and ti < len(text):
        # 첫 글자 같으면 인덱스 1씩 더해주고 다음 칸 비교
        if pattern[pi] == text[ti]:
            pi += 1
            ti += 1
        # 다르면 패턴 인덱스 초기화, 텍스트 인덱스는 처음 비교한 인덱스의 다음 인덱스로 이동
        else:
            ti = ti - pi +1
            pi = 0
        # 길이만큼 패턴 같으면 답 출력 및 브레이크
        if pi == len(pattern):
            answer = 1
            break

    print(f'#{tc} {answer}')