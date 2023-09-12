T = int(input())
for tc in range(1, T+1):
    word = input()
    # 회문이면 1, 아니면 0 출력
    answer = 0
    # 뒤집은 단어
    reversed_word = ''
    # 단어 순회하면 뒤로 저장
    for i in word:
        reversed_word = i + reversed_word
    # 회문 체크
    if word == reversed_word:
        answer = 1

    print(f'#{tc} {answer}')