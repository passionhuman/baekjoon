import sys

def dijkstra(s, V):
    U = [0] * (V + 1)
    U[s] = 1
    D[s] = 0

    for e, w in adj[s]:
        D[e] = w

    for _ in range(V):
        minV = 11
        t = 0
        for i in range(V + 1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                t = i
    U[t] = 1

    for e, w in adj[t]:
        D[e] = min(D[e], D[t] + w)

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, w = map(int, sys.stdin.readline().split())
    adj[s].append([e,w])

D = [11] * (V + 1)
dijkstra(start, V)
for i in range(1,len(D)):
    if D[i] == 11:
        print("INF")
    else:
        print(D[i])
