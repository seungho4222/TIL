T = int(input())
for tc in range(1, T+1):
    tc_num, N = map(str, input().split())
    arr = input().split()

    ZRO = []
    ONE = []
    TWO = []
    THR = []
    FOR = []
    FIV = []
    SIX = []
    SVN = []
    EGT = []
    NIN = []

    for i in arr:
        if i == 'ZRO':
            ZRO += [i]
        elif i == 'ONE':
            ONE += [i]
        elif i == 'TWO':
            TWO += [i]
        elif i == 'THR':
            THR += [i]
        elif i == 'FOR':
            FOR += [i]
        elif i == 'FIV':
            FIV += [i]
        elif i == 'SIX':
            SIX += [i]
        elif i == 'SVN':
            SVN += [i]
        elif i == 'EGT':
            EGT += [i]
        elif i == 'NIN':
            NIN += [i]

    print(tc_num)
    print(*ZRO, *ONE, *TWO, *THR, *FOR, *FIV, *SIX, *SVN, *EGT, *NIN)