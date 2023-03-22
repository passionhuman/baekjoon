from collections import deque

N, K = map(int, input().split())
if N >= K:
    print(N - K)
else:
    visited = set()
    Q = deque()
    Q.append((N, 0))
    visited.add(N)
    while Q:
        x, ans = Q.popleft()
        if x == K:
            print(ans)
            break
        for idx, nx in enumerate([2 * x, x - 1, x + 1]):
            if nx < 100001 and nx not in visited:
                visited.add(nx)
                if idx:
                    Q.append((nx, ans + 1))
                else:
                    Q.appendleft((nx, ans))