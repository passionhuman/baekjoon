import sys
T = int(sys.stdin.readline())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    for _ in range(m):
        map(int, sys.stdin.readline().split())
    print(n-1)