N = int(input())
st = "666"
N_list = []

for i in range(666, 10000667): # 임의의 큰 수까지 for문 돌리기
    if st in str(i): # 666이라는 숫자가 안에 있으면
        N_list.append(i) # N_list에 추가
        if len(N_list) == N: # N이랑 길이가 같아지면 끝내기
            break
print(N_list[N-1])