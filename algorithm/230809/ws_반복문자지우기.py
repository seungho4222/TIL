T = int(input())
for tc in range(1, T+1):
    word = list(input())
    # 반복 문자열 있을경우 2개씩 제거 => 최대 경우의 수 = 길이//2
    for _ in range(len(word)//2):
        # 앞에서 부터 확인 => 2개씩 확인하기에 길이에서 -1
        for i in range(len(word)-1):
            # 같으면 제거후 브레이크
            if word[i] == word[i+1]:
                word.pop(i)
                word.pop(i)
                break
    print(f'#{tc}', len(word))

'''
3
ABCCB
NNNASBBSNV
UKJWHGGHNFTCRRCTWLALX

'''