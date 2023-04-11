from collections import deque
N, K = map(int, input().split())

time = 1
move = [[-1, -1] for _ in range(500001)]  # 방문 시, 짝수, 홀수 최소 시간 저장
move[N][0] = 0
q = deque([N])
check = False

if N != K:
    while K < 500001:
        size = len(q)
        for _ in range(size):
            cur = q.popleft()
            for next in (cur - 1, cur + 1, cur * 2):
                if -1 < next < 500001:
                    if move[next][time % 2] < 0:
                        move[next][time % 2] = 1
                        q.append(next)
        K += time
        if K < 500001:
            if move[K][time % 2] > -1:
                check = True
                break
            time += 1
else:
    time = 0
    check = True

if check:
    print(time)
else:
    print(-1)