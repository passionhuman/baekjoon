dr = [0, 1, 0, -1] # 사방 탐색을 위한 좌표
dc = [1, 0, -1, 0]
n, m = map(int, input().split())
page = [list(map(int, input().split())) for _ in range(n)]
numbers = []
stack = []
cnt = 0

for i in range(n):
    for j in range(m):
        cnt = 1
        if page[i][j] == 1:
            r = i
            c = j
            page[r][c] = 0
            while True:
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < n and 0 <= nc < m and page[nr][nc] == 1:
                        stack.append((r, c))
                        page[nr][nc] = 0
                        cnt += 1
                        r = nr
                        c = nc
                        break

                else:
                    if stack:
                        r, c = stack.pop()
                    else:
                        break
            
            numbers.append(cnt)
print(len(numbers))
if not numbers: # 1이없을때
    print(0)
else:
    print(max(numbers))