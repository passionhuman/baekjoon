n, l = map(int, input().split())
arr = [[0,0,0]] + [list(map(int, input().split()))for _ in range(n)] + [[l,0,1]] # 처음지점넣고 , 입력받은 지점, 끝 지점 넣기
cnt = 0
for i in range(1, len(arr)):
    c, r, g = arr[i]
    cnt += (c - arr[i-1][0]) # 처음지점부터 도착한 신호등까지 cnt+ 해주기
    cnt += max(0, r-( cnt % (r+g))) # 그 다음 신호등 주기가 있으니 빨간불이면 기다리는 만큼 cnt+
print(cnt)