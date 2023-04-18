from collections import deque

while True:
    L,R,C = map(int, input().split())
    dr = [-1, 1, 0, 0, R + 1, -(R + 1)]
    dc = [0,0,-1,1,0,0]
    v = [[0] * C for _ in range(R*L+L-1)]
    ans = 0
    check = False
    if L == 0 and R == 0 and L == 0:
        break
    arr = [list(input()) for _ in range(R*L+L-1)]

    for a in arr:
        if not a:
            for _ in range(C):
                a.append(0)

    q = deque([])
    for i in range(R*L+L-1):
        for j in range(C):
            if arr[i][j] == "S":
                q.append((i,j))
                v[i][j] = 1
                break
    while q:
        size = len(q)
        for _ in range(size):
            r, c = q.popleft()
            if arr[r][c] == "E":
                q = []
                check =True
                break
            for d in range(6):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < R*L+L-1 and 0 <= nc < C and v[nr][nc] == 0 and (arr[nr][nc] == "." or arr[nr][nc] == "E"):
                    q.append((nr,nc))
                    v[nr][nc] = 1
                    if arr[nr][nc] == "E":
                        q = []
                        check = True
                        break

            if check == True:
                break
        ans += 1
    if check:
        print(f"Escaped in {ans} minute(s).")
    else:
        print("Trapped!")
    input()