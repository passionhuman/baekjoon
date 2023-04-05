def dfs():
    if len(choice) == M:
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