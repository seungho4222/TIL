import sys

sys.stdin = open('input.txt', 'r')


table = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 출력할 결과
    result = 0

    # 코드 중복 체크 방지
    dup_check = []

    # 암호코드 + 중복처리
    arr = list(set([input()[:M] for _ in range(N)]))
    # 각 줄에 대한 코드 검사
    for i in range(len(arr)):
        # i번째 줄에서 검사
        ith_row = arr[i]

        # i번째 줄 16진수 문자열을 2진수 문자열로 바꾸기
        bin_row = ''

        # i번째 문자열 2진수 변환
        for c in ith_row:
            c_hex_to_dec = int(c, 16)
            # 16진수 하나는 2진수 * 4
            for j in range(3, -1, -1):
                bin_row += '1' if c_hex_to_dec & (1 << j) else '0'

        # 2진수로 변환한 i번째 문자열에 1이 없는 경우
        if '1' not in bin_row:
            # 다음줄 검사
            continue
        # 1이 있으면 뒤에서부터 암호코드 만들기 시작
        else:
            # 0과 1의 비울 / 코드순서는 0,1,0,1
            ratio = [0] * 4
            # ratio[0] : 맨처음 0의 비율
            # ratio[1] : 두번쨰 1의 비율
            # ratio[2] : 세번쨰 0의 비율
            # ratio[3] : 마지막 1의 비율

            # 모든 암호코드는 1로 끝남 -> 오른쪽 0 제거
            bin_row = bin_row.rstrip('0')

            # 현재 i번째 줄에서 만든 숫자코드 저장
            code = []
            # 코드의 맨 끝이 1이니까 뒤에서부터 비율 계산
            for j in range(len(bin_row) - 1, -1, -1):
                if bin_row[j] == '1' and ratio[2] == 0:
                    # 마지막 1의 비율 계산 중
                    ratio[3] += 1
                elif bin_row[j] == '0' and ratio[1] == 0:
                    # 세번째 0의 비율 계산 중
                    ratio[2] += 1
                elif bin_row[j] == '1' and ratio[0] == 0:
                    # 두번째 1의 비율 계산 중
                    ratio[1] += 1
                elif bin_row[j] == '0' and bin_row[j-1] == '1':
                    # 처음 0의 비율은 계산 불필요
                    # 여기서 코드 변환 작업 시작
                    min_v = min(ratio[1:])  # 제일 작은 수 구해서 나누기
                    number = table.get((ratio[1] // min_v, ratio[2] // min_v, ratio[3] // min_v))
                    code.append(number)
                    # 비율계산 후 초기화
                    ratio = [0] * 4
                    if len(code) == 8:
                        reverse_code = code[::-1]
                        # 검증코드 계산
                        odd = reverse_code[0] + reverse_code[2] + reverse_code[4] + reverse_code[6]
                        even = reverse_code[1] + reverse_code[3] + reverse_code[5] + reverse_code[7]
                        # 계산결과 10의 배수면 올바른 코드
                        if (odd * 3 + even) % 10 == 0 and code not in dup_check:
                            # 각 자리수 더해서 답에 누적
                            result += odd + even
                            dup_check.append(code)
                        code = []
    print(f'#{tc} {result}')