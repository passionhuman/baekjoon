import sys
dr = [-1,1,0,0]
dc = [0,0,-1,1]
t = int(input())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    arr = [[0] * m for _ in range(n)]
    v = [[0] * m for _ in range(n)]
    stack = []
    ans = 0
    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        arr[y][x] = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and v[i][j] == 0:
                r = i
                c = j
                v[r][c] = 1
                ans += 1
                while True:
                    for d in range(4):
                        nr = dr[d] + r
                        nc = dc[d] + c
                        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1 and v[nr][nc] == 0:
                            stack.append((r,c))
                            r = nr
                            c = nc
                            v[r][c] = 1
                            break
                    else:
                        if stack:
                            r,c = stack.pop()
                        else:
                            break
    print(ans)
