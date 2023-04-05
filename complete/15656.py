def dfs():
    if len(choice) == M:
        print(*choice)
        return

    for i in range(len(arr)):
        choice.append(arr[i])
        dfs()
        choice.pop()

N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
choice = []
dfs()