n, m = map(int, input().split())
arr = [list(map(str, input())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == ".":
            cnt = 0
            c = j
            while True:
                c -= 1
                cnt += 1
                if 0 <= c < m and arr[i][c] == "c":
                    arr[i][j] = cnt
                    break
                elif c < 0 or c >= m:
                    arr[i][j] = -1
                    break
for i in range(n):
    for j in range(m):
        if arr[i][j] == "c":
            arr[i][j] = 0
for i in arr:
    print(*i)