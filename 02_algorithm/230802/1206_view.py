T = 10
for tc in range(1, T + 1):
    N = int(input())
    bld = list(map(int, input().split()))

    # 조망권을 가지는 세대 수
    count = 0

    # 반복문을 통해 각 빌딩의 조망권이 확보된 세대의 개수 카운트 => 중첩 반복문

    # 중첩 반복문을 사용할 때는 밖 반복문 / 안 반복문
    # 한 빌딩의 모든 세대를 다 확인하고 다음 빌딩으로 넘어갈 것
    # 밖의 반복문은 빌딩의 개수 / 안의 반복문의 빌딩의 높이

    for i in range(2, N - 2):  # 양쪽 2칸씩은 무조건 높이가 0 => 확인 불필요
        # bld[i] = i 번째 빌딩의 높이
        height = bld[i]
        for j in range(height, -1, -1):  # 시작 = 꼭대기. 끝 = 0, -1
            # 현재 i번째 건물의 층수 j
            # j 층에서 양쪽 2칸을 확인한 다음 조망권이 있으면 count +1

            # 왼쪽 -1, -2 건물의 높이, 오른쪽 +1, +2 건물의 높이 확인
            # 현재 j 층이 왼쪽과 오른쪽 건물의 높이보다 높아야 조망권 ok
            # 왼쪽 -1 => bld[i-1]
            # 왼쪽 -2 => i-2, 오른쪽 +1 => i+1, 오른쪽 +2 => i+2
            if j > bld[i - 1] and j > bld[i - 2] and j > bld[i + 1] and j > bld[i + 2]:
                count += 1
            else:
                # 조망권이 없는 경우 밑층은 확인할 필요 없음
                break

    print(f'#{tc}', count)

T = 10
for tc in range(1, T + 1):
    N = int(input())
    bld = list(map(int, input().split()))
    count = 0

    for i in range(2, N - 2):
        height = bld[i]
        for j in range(height, -1, -1):
            if j > bld[i - 1] and j > bld[i - 2] and j > bld[i + 1] and j > bld[i + 2]:
                count += 1
            else:
                break
    print(f'#{tc}', count)