for _ in range(10):
    tc = int(input())
    fs = input()
    s = input()
    cnt = 0
    for i in range(len(fs), len(s) + 1):
        if s[i - len(fs):i] == fs:
            cnt += 1
    print(f"#{tc}", cnt)
