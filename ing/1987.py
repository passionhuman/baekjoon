from collections import deque
dr = [-1,1,0,0]
dc = [0,0,-1,1]
n, m = map(int,input().split())
arr = [list(input()) for _ in range(n)]
visited = []
visited.append(arr[0][0])
q = deque([(0, 0)])
stack = []
cnt = 0
while q:
    size = len(q)
    for _ in range(size):
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] not in visited:
                q.append((nr,nc))
                stack.append(arr[nr][nc])
        for i in range(len(stack)):
            visited.append(stack[i])
        stack = []
    cnt += 1
print(cnt)

