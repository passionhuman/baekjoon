import sys
from collections import deque
import copy
dr = [-1,1,0,0]
dc = [0,0,-1,1]
N,M = map(int,sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
water = deque([])
ans = 0
check = 0
v_temp = [[0] * M for _ in range(N)]
for k in range(N):
    for l in range(M):
        if arr[k][l] == 0:
            water.append((k, l))

while water:
    stack = []
    v = copy.deepcopy(v_temp)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and v[i][j] == 0:
                r = i
                c = j
                v[i][j] = 1
                cnt += 1
                if cnt > 1:
                    break
                while True:
                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]
                        if 0 <= nr < N and 0 <= nc < M and v[nr][nc] == 0 and arr[nr][nc] != 0:
                            stack.append((r,c))
                            r = nr
                            c = nc
                            v[r][c] = 1
                            break
                    else:
                        if stack:
                            r, c = stack.pop()
                        else:
                            break
    if cnt > 1:
        break
    size = len(water)
    for _ in range(size):
        qr,qc = water.pop()
        for qd in range(4):
            nqr = qr + dr[qd]
            nqc = qc + dc[qd]
            if 0 <= nqr < N and 0 <= nqc < M and arr[nqr][nqc] > 0:
                arr[nqr][nqc] -= 1
    ans += 1
    check = 0
    for k2 in range(N):
        for l2 in range(M):
            if arr[k2][l2] == 0:
                water.append((k2, l2))
            else:
                check = 1
    if check == 0:
        break


if check == 1:
    print(ans)
else:
    print(0)