from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cnt = 0
q = deque([])
ans = []
check = 0
perfect = 0

for t in tomato:
    for a in t:
        ans.append(a)

if 0 not in ans and 1 in ans:
    perfect = 1


for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i,j))
            visited[i][j] = 1
while q:
    size = len(q)
    for _ in range(size):
        r, c = q.popleft()
        tomato[r][c] = 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0 and tomato[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = 1
    cnt += 1

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            check = 1

if perfect == 1:
    print(0)
elif check == 1:
    print(-1)
else:
    print(cnt - 1)
