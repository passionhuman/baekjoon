dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
m, n = map(int, input().split())
find = int(input())
arr = [[0] * m for _ in range(n)]
cnt = 1
r = n - 1
c = d = 0
check = False
while True:
    arr[r][c] = cnt
    nr = r + dr[d]
    nc = c + dc[d]
    if cnt == n * m:
        break
    elif 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
        r = nr
        c = nc
        cnt += 1
    else:
        d += 1
        if d == 4:
            d = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == find:
            ans_r = j
            ans_c = i
            check = True
            break

if check:
    print(ans_r + 1,n - ans_c)
else:
    print(0)
