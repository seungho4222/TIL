# 암호코드(16진수) 찾기
def search():
    hex_string = []
    for r in range(N):
        for x in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']:
            if x in arr[r]:
                if arr[r] not in hex_string:
                    hex_string.append(arr[r])
                    break
    zero_ck = []
    for i in hex_string:
        for j in range(len(i)-1, -1, -1):
            if i[j] != '0':
                zero_ck.append(''.join(i[:j+1]))
                break
    return zero_ck


# 2진수 변환
def bin_change(hex_string):
    # 16진수 2진수 변환
    l = len(hex_string) * 4
    x = int(hex_string, 16)
    bin_string = ''
    for i in range(l - 1, -1, -1):
        bin_string += '1' if x & (1 << i) else '0'
    # 암호코드 부분 자르기
    len_bin = len(bin_string)
    code = ''
    k = len_bin // 56
    for c in range(len_bin - 1, -1, -1):
        if bin_string[c] == '1':
            code += bin_string[c - (55 * k):c + 1]
            break
    return code


# 8자리 숫자 변환
def nums_change(c):
    l = len(c)
    k = len(c) // 56
    # 코드별 비율
    code_ratio = []
    for i in range(0, l, 7 * k):
        r = []  # 코드 비율 4자리 저장
        ratio = 0  # 코드 비율 체크
        check = 0  # 0,1 체크
        for j in range(0, 7 * k, k):
            if int(c[i + j]) == check:
                ratio += 1
            else:  # 체크가 다르면 코드 비율 저장하고 값 변경
                r.append(ratio)
                ratio = 1
                check = (check + 1) % 2
        # 마지막 코드 비율 추가
        r.append(ratio)
        # 튜플 변경 후 한자리 코드 추출
        code_ratio.append(tuple(r))
    # 숫자 변경
    nums = []
    for j in code_ratio:
        nums.append(pat[j])
    return nums


def test(nums):
    # 올바른 암호코드 판단
    calc1 = 0  # 홀수번째 1, 3, 5, 7
    calc2 = 0  # 짝수번째 2, 4, 6, 8
    for i in range(7):
        if i % 2 == 0:
            calc1 += nums[i]
        else:
            calc2 += nums[i]
    sum_calc = (calc1 * 3) + calc2 + nums[7]
    # 10의 배수면 코드의 합 출력
    if sum_calc % 10 == 0:
        return True
    else:
        return False


# 패턴 비율 별 숫자 변환 표
pat = {
    (3, 2, 1, 1): 0,
    (2, 2, 2, 1): 1,
    (2, 1, 2, 2): 2,
    (1, 4, 1, 1): 3,
    (1, 1, 3, 2): 4,
    (1, 2, 3, 1): 5,
    (1, 1, 1, 4): 6,
    (1, 3, 1, 2): 7,
    (1, 2, 1, 3): 8,
    (3, 1, 1, 2): 9}

T = int(input())
for tc in range(1, T + 1):
    # N: 가로, M: 세로
    N, M = map(int, input().split())
    arr = [list(input()[:M]) for _ in range(N)]
    # 2진수 암호코드 추출
    bin_code = []
    for i in search():
        bin_code.append(bin_change(i))
    # 8자리 숫자 변환

    ans = 0
    for i in bin_code:
        eight_nums = nums_change(i)
        if test(eight_nums):
            ans += sum(eight_nums)

    print(f'#{tc} {ans}')
