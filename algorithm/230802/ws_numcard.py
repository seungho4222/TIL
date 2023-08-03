T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = input()
    arr = [0] * 10
    # 가장 많은 카드의 숫자와 장 수 초기화
    max_num = 0
    max_cnt = 0
    # 카드 장수 배열 생성
    for i in nums:
        arr[int(i)] += 1

    for j in range(10):
        if max_cnt <= arr[j]:
            max_cnt = arr[j]
            max_num = j

    print(f'#{tc}', max_num, max_cnt)
