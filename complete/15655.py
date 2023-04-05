def dfs():
    if len(choice) == M:
        temp = choice[0]
        for i in range(M):
            if temp > choice[i]:
                return
            else:
                temp = choice[i]
        print(*choice)
        return

    for i in range(len(arr)):
        if v[i] == 0:
            choice.append(arr[i])
            v[i] = 1
            dfs()
            v[i] = 0
            choice.pop()

N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
choice = []
v = [0] * (N + 1)
dfs()