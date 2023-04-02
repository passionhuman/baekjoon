import sys
from collections import deque
def bfs(n):
    cnt = 0
    q = deque() # BFS를 위한 queue
    q.append(n)
    v[n] = 1
    while q:
        size = len(q)
        for _ in range(size):
            c = q.popleft()
            if c == K:
                return cnt # 몇 초 걸리는지 return
            for d in (c-1, c+1, c*2):
                if 0 <= d < 100001 and v[d] == -1:
                    q.append(d)
                    v[d] = 1 # 이건 방문처리
                    moved[d] = c # 이건 어디서 숫자가 왔는지 즉, 2 -> 4 갔으면 moved[4]에 2저장
        cnt += 1
def move(m): #
    ans_lst = []
    temp = moved[m]
    ans_lst.append(temp)
    while True:
        if moved[temp] == -1: # -1이면 도착했다는거니
            return ans_lst[::-1] # 거꾸로 뒤집어서 출력
        else:
            ans_lst.append(moved[temp]) # 어디서 왔는지 담아주고
            temp = moved[temp] # 그 숫자는 또 어디로 갔는지 temp 최신화
N, K = map(int, sys.stdin.readline().split())
v = [-1] * 100001
moved = [-1] * 100001
moved[N] = -1
if N == K:
    print(0)
    print(N)
else:
    print(bfs(N))
    print(*(move(K) + [K]))