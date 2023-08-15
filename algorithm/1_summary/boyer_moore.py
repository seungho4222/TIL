def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)

    # 패턴의 마지막 문자의 앞문자부터 역순으로 번호 지정 -> sky에서 {s:2, k:1}
    skip_table = {}
    for i in range(m - 1):
        skip_table[pattern[i]] = m - i - 1

    i = m - 1  # 텍스트와 패턴을 비교할 인덱스 초기화
    j = m - 1  # 패턴의 끝부터 비교할 인덱스 초기화
    # cnt = 0    # 패턴 이동 횟수 카운트
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i  # 패턴이 텍스트와 일치하는 위치를 찾음
                # return cnt # 이동횟수 산정시
            else:
                i -= 1
                j -= 1
        else:
            # 일치하지 않는 경우, skip_table을 이용하여 패턴을 뒤로 이동
            skip_val = skip_table.get(text[i], m)
            i += skip_val
            j = m - 1
            # cnt += 1  # 이동 카운트

    return -1  # 패턴이 텍스트에 없는 경우


# 예시 사용
text = "ABABABCABABABCABABABC"
pattern = "ABC"
result = boyer_moore_search(text, pattern)
print(result)  # 출력: 4 (패턴이 처음 나타나는 위치)