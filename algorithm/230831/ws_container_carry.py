T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N: 컨테이너 수, M: 트럭 수
    container = sorted(list(map(int, input().split())), reverse=True)  # 내림차순 정렬
    truck = sorted(list(map(int, input().split())), reverse=True)  # 내림차순 정렬

    cnt = 0
    for t in truck:  # 트럭보다
        for c in container:  # 컨테이너가
            if t >= c:  # 작으면
                cnt += c  # 컨테이너 옮기고
                container.remove(c)  # 해당 컨테이너 제거
                break
    print(f'#{tc} {cnt}')
