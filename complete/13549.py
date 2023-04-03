import sys
from collections import deque
def bfs(n):
    cnt = 0
    q = deque() # BFS를 위한 queue
    q.append(n)
    v[n] = 1
    idx_cnt = 0
    while q:
        size = len(q)
        for _ in range(size):
            c = q.popleft()
            if c == K:
                print(idx_cnt)
                return cnt # 몇 초 걸리는지 return
            for idx,d in enumerate([c-1, c+1, c*2]):
                if 0 <= d < 100001 and v[d] == -1:
                    if idx == 2:
                        idx_cnt += 1
                    q.append(d)
                    v[d] = 1 # 이건 방문처리
        cnt += 1
N, K = map(int, sys.stdin.readline().split())
v = [-1] * 100001
if N == K:
    print(0)
else:
    print(bfs(N))
