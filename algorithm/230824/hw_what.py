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


def hex_bin(arr_row):
    for i in range(M-1, -1, -1):
        if arr_row[i] != '0':
            hex_string = ''.join(arr_row)
            l = len(hex_string) * 4
            x = int(hex_string, 16)
            bin_string = ''
            for j in range(l - 1, -1, -1):
                bin_string += '1' if x & (1 << j) else '0'
            for k in range(len(bin_string)-1,-1,-1):
                if bin_string[k] == '1':
                    return list(bin_string[:k+1])
    return 0


def check(b_code):
    for k in range(len(b_code)):
        if b_code[k] != '0':
            return 1
    return 0

def code_change(b_code):
    nums = []
    for i in range(8):
        n4 = 0
        n3 = 0
        n2 = 0
        while True:
            x = b_code.pop()
            if x == '0':
                continue
            else:
                b_code.append(x)
                break
        while True:
            x = b_code.pop()
            if x == '1':
                n4 += 1
            else:
                b_code.append(x)
                break
        while True:
            x = b_code.pop()
            if x == '0':
                n3 += 1
            else:
                b_code.append(x)
                break
        while True:
            x = b_code.pop()
            if x == '1':
                n2 += 1
            else:
                b_code.append(x)
                break
        check = min(n4, n3, n2) * 7
        n1 = check - n4 - n3 - n2
        for i in range(n1):
            b_code.pop()
        ratio = min(n2,n3,n4)
        n1 //= ratio
        n2 //= ratio
        n3 //= ratio
        n4 //= ratio
        nums = [pat[(n1, n2, n3, n4)]] + nums
    save.append(''.join(map(str,nums)))
    return nums, b_code


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


T = int(input())
for tc in range(1, T + 1):
    # N: 가로, M: 세로
    N, M = map(int, input().split())
    arr = [input()[:M] for _ in range(N)]
    arr = list(set(arr))
    # 이진법 변경한 열
    bin_code = []
    for i in arr:
        x = hex_bin(i)
        if x and x not in bin_code:
            bin_code.append(x)

    save = []
    while bin_code:
        i = bin_code.pop()
        if check(i):
            nums, temp = code_change(i)
            bin_code.append(temp)

    ans = 0
    save = list(set(save))
    for i in save:
        x = list(map(int, i))
        if test(x):
            ans += sum(x)

    print(f'#{tc} {ans}')
