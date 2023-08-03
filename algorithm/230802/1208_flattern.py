# import sys
#
# sys.stdin = open('input.txt', 'r')


T = 10
for tc in range(1, T + 1):
    dump = int(input())
    box = list(map(int, input().split()))

    arr = [0] * 101     # 상자층별 개수 저장
    for i in box:
        arr[i] += 1

    high_box, low_box = 100, 1

    # 덤프횟수만큼 가장 높은 곳의 박스를 가장 낮은 곳으로 이동

    for j in range(100,0,-1):
        for k in range(1,101):
            while dump and arr[j] and arr[k]:   # 덤프횟수, 최고점 및 최저점 상자층 개수 계산
                arr[j] -= 1     # 최고점에서 하나 빼면
                arr[j-1] += 1   # 최고점-1의 박스층 개수 +1
                arr[k] -= 1     # 최저점에서 하나 빼면
                arr[k+1] += 1   # 최저점+1의 박스층 개수 +1
                dump -= 1       # 덤프 카운트
                if arr[j] == 0: high_box = j - 1    # 위치이동후 최고점 상자층 저장
                else: high_box = j
                if arr[k] == 0: low_box = k + 1     # 위치이동후 최저점 상자층 저장
                else: low_box = k
            if dump == 0 or arr[j] == 0:    # 탈출
                break
        if dump == 0:   # 탈출
            break

    print(f'#{tc}', high_box - low_box)