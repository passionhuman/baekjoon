def dfs():
    if len(choice) == M:
        print(*choice) # 선택된 배열이 M개와 같아졌을 경우 출력 후 return
        return
    pre = 0 # 내가 어떤 원소 담아줬는지 체크할 변수
    for i in range(len(arr)):
        if v[i] == 0 and pre != arr[i]: # 똑같은 변수를 고르면 중복순열이 되어버리므로
            choice.append(arr[i]) # 선택한 원소 담고
            v[i] = 1 # 방문처리 해주고
            pre = arr[i] # 최근에 담은 원소 pre에 담아주기
            dfs()
            v[i] = 0 # 방문처리 원복
            choice.pop() # 다른 원소 넣기 위해 pop

N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
choice = []
v = [0] * (N + 1) # 방문체크 배열 선언
dfs()
