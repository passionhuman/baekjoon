dr = [-1,1,0,0]
dc = [0,0,-1,1]
def dfs(r,c):
    if v[r][c]:
        return v[r][c]
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N  and arr[r][c] < arr[nr][nc]:
            v[r][c] = max(v[r][c], dfs(nr,nc)+1)
    return v[r][c]

import sys
sys.setrecursionlimit(10**9)
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
v = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        dfs(i,j)
print(max(map(max,v))+1)
