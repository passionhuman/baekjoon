import sys
from collections import deque
def bfs(n):
    cnt = 0
    q = deque()
    q.append(n)
    v[n] = 1
    while q:
        size = len(q)
        for _ in range(size):
            c = q.popleft()
            if c == K:
                return cnt
            for d in (c-1, c+1, c*2):
                if 0 <= d < 100001 and v[d] == 0:
                    q.append(d)
                    v[d] = 1
        cnt += 1
N, K = map(int, sys.stdin.readline().split())
v = [0] * 100001
print(bfs(N))