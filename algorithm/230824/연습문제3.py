pat = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9
}

hex1 = '0DEC'
hex2 = '0269FAC9A0'


def find_pattern(hex_string):
    l = len(hex_string) * 4
    x = int(hex_string, 16)

    bin_string = ''
    for i in range(l - 1, -1, -1):
        bin_string += '1' if x & (1 << i) else '0'

    code = []
    for j in range(l - 1, -1, -1):
        if bin_string[j] == '1':
            idx = j
            break
    for k in range(idx, -1, -6):
        if k < 5:
            break
        code.append(pat[bin_string[k - 5:k + 1]])
    return code[::-1]


print(*find_pattern(hex1))
print(*find_pattern(hex2))
