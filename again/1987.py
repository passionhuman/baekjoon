import sys
dr = [1,-1,0,0]
dc = [0,0,-1,1]
n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline()) for _ in range(n)]
visited = set()
visited.add(arr[0][0])
r = c = 0
cnt = 0
max_cnt = 0
def dfs(r, c, cnt):
    global ans
    global max_cnt
    if cnt > max_cnt:
        max_cnt = cnt
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] not in visited:
            visited.add(arr[nr][nc])
            dfs(nr, nc, cnt + 1)
            visited.remove(arr[nr][nc])
dfs(0,0,1)
print(max_cnt)