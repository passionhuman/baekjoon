import sys
from collections import deque
def bfs(n):
    q = deque()
    q.append(n)
    while q:
        c = q.popleft()
        if c == K:
            return v[c]
        for d in (c-1, c+1, c*2):
            if 0 <= d < 100001 and v[d] == 0:
                if d == c * 2 and d != 0:
                    q.appendleft(d)
                    v[d] = v[c]
                else:
                    q.append(d)
                    v[d] = v[c] + 1
N, K = map(int, sys.stdin.readline().split())
v = [0] * 100001
if N == K:
    print(0)
else:
    print(bfs(N))