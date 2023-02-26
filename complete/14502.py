import sys
from collections import deque
import copy
stack = []
q = deque([])
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt = 0
max_cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            q.append((i,j))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            arr[i][j] = 1

            for i2 in range(n):
                for j2 in range(m):
                    if arr[i2][j2] == 0:
                        arr[i2][j2] = 1

                        for i3 in range(n):
                            for j3 in range(m):
                                if arr[i3][j3] == 0:
                                    arr[i3][j3] = 1
                                    q2 = copy.deepcopy(q)
                                    while q2:
                                        size = len(q2)
                                        for _ in range(size):
                                            r, c = q2.popleft()
                                            for d in range(4):
                                                nr = r + dr[d]
                                                nc = c + dc[d]
                                                if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
                                                    q2.append((nr,nc))
                                                    arr[nr][nc] = 2
                                                    stack.append((nr, nc))
                                    for a in range(n):
                                        for b in range(m):
                                            if arr[a][b] == 0:
                                                cnt += 1
                                    if cnt > max_cnt:
                                        max_cnt = cnt
                                    cnt = 0
                                    while stack:
                                        c, d = stack.pop()
                                        arr[c][d] = 0
                                    arr[i3][j3] = 0
                        arr[i2][j2] = 0
            arr[i][j] = 0
print(max_cnt)