import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    field = [list(input()) for _ in range(H)]
    N = int(input())
    for i in input():
        ...

    print(field)