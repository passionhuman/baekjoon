from collections import deque
import sys
n = int(sys.stdin.readline()) # 시간줄이기
tree = [[] for _ in range(n+1)] # 인접리스트
visited = [0] * (n + 1) # visited 처리
q = deque([])
ans = {} # 정답 담을 딕셔너리
for i in range(n-1): # 간선처리
    s, e = map(int, sys.stdin.readline().split())
    tree[s].append(e)
    tree[e].append(s)

q.append(1)
visited[1] = 1
while q: # bfs로 돌리기
    size = len(q)
    for _ in range(size):
        s = q.popleft()
        for t in tree[s]:
            if visited[t] == 0:
                ans[t] = s
                visited[t] = 1
                q.append(t)
for i in range(2, n+1): # 출력은 2번 노드부터
    print(ans[i])