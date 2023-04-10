from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

n, m = map(int, input().split())
maze = [list(input()) for _ in range(n)]
v = [[0] * m for _ in range(n)]
fv = [[0] * m for _ in range(n)]
cnt = 0
check = False
j_queue = deque([])
f_queue = deque([])
for i in range(n):
    for j in range(m):
        if maze[i][j] == "J":
            j_queue.append((i,j))
            v[i][j] = 1
        elif maze[i][j] == "F":
            f_queue.append((i,j))
            fv[i][j] = 1

while j_queue:
    f_size = len(f_queue)
    for _ in range(f_size):
        fr, fc, = f_queue.popleft()
        for d in range(4):
            nfr = fr + dr[d]
            nfc = fc + dc[d]
            if 0 <= nfr < n and 0 <= nfc < m and fv[nfr][nfc] == 0 and maze[nfr][nfc] != "#":
                f_queue.append((nfr,nfc))
                fv[nfr][nfc] = 1

    size = len(j_queue)
    for _ in range(size):
        r,c = j_queue.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 > nr or nr >= n or nc < 0 or nc >= m:
                check = True
                j_queue = []
                break


            if 0 <= nr < n and 0 <= nc < m and v[nr][nc] == 0 and maze[nr][nc] == "." and fv[nr][nc] == 0:
                j_queue.append((nr,nc))
                v[nr][nc] = 1
        if check == True:
            break
    cnt += 1

if check:
    print(cnt)
else:
    print("IMPOSSIBLE")