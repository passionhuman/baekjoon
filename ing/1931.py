import sys
N = int(sys.stdin.readline())
ans = 1
time = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
time.sort(key=lambda x: x[0])
time.sort(key=lambda x: x[1])
end_time = time.pop(0)[1]
while time:
    s, e = time.pop(0)
    if end_time <= s:
        end_time = e
        ans += 1
print(ans)