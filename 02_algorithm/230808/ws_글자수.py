T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    # 가장 많은 글자 개수
    max_str_cnt = 0
    # 글자 비교
    for i in str1:
        # 글자 개수
        str_cnt = 0
        for j in str2:
            if i == j:
                str_cnt += 1
        # 글자 개수 비교 및 갱신
        if max_str_cnt < str_cnt:
            max_str_cnt = str_cnt

    print(f'#{tc}', max_str_cnt)