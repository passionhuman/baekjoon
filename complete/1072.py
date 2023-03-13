x, y = map(int, input().split())
ans = int(y * 100 / x) # 게임승률
s = 1 # 이분탐색 범위 제일 낮은 수
e = x # 이분탐색 범위 제일 높은 수
res = [] # 정답 담을 배열
while s <= e: # 이분 탐색 시작
    mid = (s + e) // 2 # mid 값으로 게임 몇 판 더해줄지 정하기
    temp = int((y + mid) * 100 / (x + mid))
    if ans != temp: # 게임승률이 달라졌다는거니
        e = mid -1 # mid 크기를 줄여보기
        res.append(mid)
    else:
        s = mid + 1 # 안달라졌으면 mid 값 키우기
if res:
    print(s)
else:
    print(-1)