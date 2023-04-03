import sys
from collections import deque
def bfs(n,temp):
    global K
    cnt = 0
    q = deque()
    q.append(n)

    while q:
        size = len(q)
        for _ in range(size):
            c = q.popleft()
            if K > 500000:
                return -1
            if c == K:
                print(K)
                return cnt
            for d in (c-1, c+1, c*2):
                if 0 <= d < 500001:
                    q.append(d)
        cnt += 1
        K += temp
        temp += 1

N, K = map(int, sys.stdin.readline().split())
v[]
print(bfs(N,1))