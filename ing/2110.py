import sys
n, c = map(int, sys.stdin.readline().split())
lst = []
for i in range(n):
    temp = int(sys.stdin.readline())
    lst.append(temp)
lst.sort()
start = 1
end = lst[-1] - lst[0]
ans = 0
while start <= end:
    cur = lst[0] # 현재 설치되어있는 공유기 위치
    cnt = 1 # 현재 설치한 공유기 개수
    mid = (start + end) // 2 # 설치할 공유기와 설치된 공유기 거리
    for i in range(1, n):
        if lst[i] - cur >= mid:
            cnt += 1
            cur = lst[i]
    if cnt >= c:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
print(ans)