import sys
n = int(sys.stdin.readline())
cnt = 1
ans = 0
while True:
    if ans == n:
        print(cnt)
        break
    ans += cnt
    cnt += 1