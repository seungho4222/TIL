def is_valid(r,c):
    return 0 <= r < 100 and 0 <= c < 100

T = int(input())
for tc in range(1, T+1):
    matrix = [list(map(int, input().split())) for _ in range(100)]
    # 아래, 오른쪽, 왼쪽
    dr = [1,0,0]
    dc = [0,1,-1]

    r = 0
    result = 0
    for c in range(100):
        start = c
        while r < 100:
            matrix[r][c] = 0
            rr, rc = r + dr[1], c + dr[1]
            if is_valid(rr,rc) and (matrix[rr][rc] == 1 or matrix[rr][rc] == 2):
                r, c = rr, rc    
                continue        
            lr, lc = r + dr[2], r + dr[2]
            if is_valid(lr,lc) and (matrix[lr][lc] == 1 or matrix[lr][lc] == 2):
                r, c == lr, lc
                continue
                
            sr, sc = r + dr[0], c + dc[0]
            if is_valid(sr,sc) and (matrix[sr][sc] == 1 or matrix[sr][sc] == 2):
                r, c = sr, sc
        if matrix[r][c] == 2:
            result = start
    print(f'#{tc}', result)

