dr = [-1, 1, 0, 0] # 사방 탐색을 위한 좌표
dc = [0, 0, -1, 1]
n = int(input())
apart = [list(map(str, input())) for _ in range(n)]
numbers = []
stack = []

for i in range(n):
    for j in range(n):
        cnt = 1 # 본인을 포함한 단지의 수
        if apart[i][j] == "1":
            r = i
            c = j
            apart[r][c] = "0"
            while True:
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < n and 0 <= nc < n and apart[nr][nc] == "1":
                        stack.append((r, c))
                        apart[nr][nc] = "0"
                        r = nr
                        c = nc
                        cnt += 1 # 같은 단지 한 개 추가당 cnt + 1
                        break

                else:
                    if stack:
                        r, c = stack.pop()
                    else:
                        break
            numbers.append(cnt)                
numbers = sorted(numbers)
print(len(numbers))
print(*numbers, sep = '\n')