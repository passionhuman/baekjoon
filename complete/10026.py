dr = [-1,1,0,0]
dc = [0,0,-1,1]
n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
visited2 = [[0] * n for _ in range(n)]
stack = []
stack2 = []
cnt = 0
cnt2= 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            r = i
            c = j
            visited[r][c] = 1
            cnt += 1
            while True:
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0 and arr[i][j] == arr[nr][nc]:
                        stack.append((r,c))
                        r = nr
                        c = nc
                        visited[r][c] = 1
                        break

                else:
                    if stack:
                        r, c = stack.pop()
                    else:
                        break

for i in range(n):
    for j in range(n):
        if visited2[i][j] == 0:
            r = i
            c = j
            visited2[r][c] = 1
            cnt2 += 1
            while True:
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < n and 0 <= nc < n and visited2[nr][nc] == 0 and (arr[i][j] == arr[nr][nc] or (arr[i][j] == "R" and arr[nr][nc] == "G") or (arr[i][j] == "G" and arr[nr][nc] == "R")):
                        stack2.append((r,c))
                        r = nr
                        c = nc
                        visited2[r][c] = 1
                        break

                else:
                    if stack2:
                        r, c = stack2.pop()
                    else:
                        break
print(cnt, cnt2)