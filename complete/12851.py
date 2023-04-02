import sys
from collections import deque
def bfs(n):
    global order
    global ans
    cnt = 0
    q.append(n)
    v[n] = 1
    while q:
        size = len(q)
        for _ in range(size):
            c = q.popleft()
            v[c] = 1
            if c == K:
                ans = cnt
                order += 1
            for d in (c-1, c+1, c*2):
                if 0 <= d < 100001 and v[d] == 0:
                    q.append(d)
        if ans != 0:
            return
        cnt += 1
N, K = map(int, sys.stdin.readline().split())
v = [0] * 100001
q = deque()
ans = 0
order = 0
bfs(N)
print(ans, order)
