n = int(input()) # 몇 명인지 입력받고
go = list(map(int, input().split())) # 몇 번 뽑았는지 입력받기
human = [i for i in range(1,n+1)] # 처음에는 온 순서 리스트 생성
for i in range(1, n):
    move, cur = go[i], human[i] # 몇 칸 가야하는지, 몇 번째 사람인지 보고
    for j in range(move):
        human[cur-2], human[cur -1] = human[cur-1], human[cur-2] # 가야하는만큼 앞뒤로 바꿔주기
        cur -= 1
print(*human)