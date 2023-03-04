dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
n = int(input())
arr = [[0] * 102 for _ in range(102)]
visited = [[0] * 102 for _ in range(102)]
ans = 0
for _ in range(n):
    c, r = map(int, input().split())
    for i in range(r+1, r + 11):
        for j in range(c+1, c + 11):
            arr[i][j] = 1
for i in range(102):
    for j in range(102):
        if arr[i][j] == 0:
            for d in range(4):
                nr = i + dr[d]
                nc = j + dc[d]
                if 0 <= nr < 102 and 0 <= nc < 102 and arr[nr][nc] == 1:
                    visited[nr][nc] += 1
for i in visited:
    ans += sum(i)
print(ans)