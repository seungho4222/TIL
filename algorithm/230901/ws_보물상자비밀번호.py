T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # N: 숫자개수, K: 크기순서(출력값인덱스)
    hex_num = list(input())  # N개의 16진수
    nums = []  # 생성 가능한 수
    for _ in range(N//4):  # 4의 배수이므로 N//4이상 돌리면 숫자 중복
        for i in range(0, N, N//4):  # 4등분 하기
            num = ''.join(hex_num[i:i+N//4])  # 숫자 만들기
            if num not in nums:  # 중복아니면 스택
                nums.append(num)
        hex_num.append(hex_num.pop(0))  # 뚜껑 회전
    result = sorted(nums, reverse=True)[K-1]  # 크기 순 정렬 후 K번째 값 추출
    print(f'#{tc} {int(result,16)}')  # 10진수 변경값 출력
