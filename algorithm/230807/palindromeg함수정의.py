# 회문 검사
def palindrome(x):
    for i in range(len(x)//2):
        if x[i] != x[len(x) - i - 1]:
            return False
    return True


print(palindrome('racecar'))