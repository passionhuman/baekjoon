def dfs():
    if len(choice) == M:
        temp = choice[0]
        for i in range(1, M):
            if temp > choice[i]:
                return
            else:
                temp = choice[i]
        print(*choice)
        return

    for i in range(len(arr)):
        choice.append(arr[i])
        dfs()
        choice.pop()

N,M = map(int, input().split())
arr = [i for i in range(1,N+1)]
choice = []
dfs()