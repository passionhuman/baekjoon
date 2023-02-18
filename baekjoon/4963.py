dr = [-1, 1, 0, 0, -1, -1, 1, 1] # 팔방 탐색을 위한 좌표
dc = [0, 0, -1, 1, -1, 1, -1, 1]
while True: # 많은 케이스들 입력 받기 위해
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    island = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    stack = []
 
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1: # 땅이면 while 들어가즈아
                island[i][j] = 0 # visited 처리
                r = i
                c = j
                while True:
                    for d in range(8): # 다음 좌표 받고
                        nr = r + dr[d]
                        nc = c + dc[d]
                        if 0 <= nr < h and 0 <= nc < w and island[nr][nc] == 1:
                            stack.append((r ,c)) # 스택에 전에 꺼 좌표 넣고
                            island[nr][nc] = 0 # visited 처리
                            r = nr
                            c = nc
                            break
                    else:
                        if stack:
                            r, c = stack.pop() # 해당 좌표에선 8방탐색해도 없다는 거니까 전에 좌표로 돌아가기
                        else:
                            break
                cnt += 1
    print(cnt)