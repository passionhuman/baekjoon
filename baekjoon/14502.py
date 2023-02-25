from collections import deque # bfs로 접근
import copy
stack = []
q = deque([])
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
max_cnt = 0
for i in range(n): # 바이러스가 담긴 좌표 담기
    for j in range(m):
        if arr[i][j] == 2:
            q.append((i,j))

for i in range(n): # 첫 번째 벽을 칠 곳
    for j in range(m):
        if arr[i][j] == 0:
            arr[i][j] = 1

            for i2 in range(n): # 두 번째 벽을 칠 곳
                for j2 in range(m):
                    if arr[i2][j2] == 0:
                        arr[i2][j2] = 1

                        for i3 in range(n): # 세 번째 벽을 칠 곳
                            for j3 in range(m):
                                if arr[i3][j3] == 0:
                                    arr[i3][j3] = 1
                                    q2 = copy.deepcopy(q)
                                    while q2:
                                        size = len(q2)
                                        for _ in range(size):
                                            r, c = q2.popleft()
                                            for d in range(4): # bfs로 바이러스 근접한 0으로 된 곳은 다 2로 만들어주기
                                                nr = r + dr[d]
                                                nc = c + dc[d]
                                                if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
                                                    q2.append((nr,nc))
                                                    arr[nr][nc] = 2
                                                    stack.append((nr, nc)) # 2로 만들었던곳을 나중에 다시 0으로 만들어주기 위한 스택
                                    for a in range(n): # 바이러스로 전파가 안된 곳 세기
                                        for b in range(m):
                                            if arr[a][b] == 0:
                                                cnt += 1
                                    if cnt > max_cnt: # 만약 지금 벽친 세 군데가 최대 안전지역이 된다면 최대 안전지역 갱신해주기
                                        max_cnt = cnt
                                    cnt = 0 # cnt 초기화
                                    while stack: # 0 -> 2 로 바꿔줬던 부분 다시 0으로 바꿔주기
                                        c, d = stack.pop()
                                        arr[c][d] = 0
                                    arr[i3][j3] = 0 # 세 번째 벽친 곳 다시 0으로 만들어주기
                        arr[i2][j2] = 0 # 두 번째 벽친 곳 다시 0으로 만들어주기
            arr[i][j] = 0 # 첫 번째 벽친 곳 다시 0으로 만들어주기
print(max_cnt) # 최댓값 뽑기