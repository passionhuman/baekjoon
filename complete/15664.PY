def dfs():
    if len(choice) == M:
        temp = choice[0]
        for i in range(1, M):
            if temp > choice[i]:
                return
            else:
                temp = choice[i]
        print(*choice) #
        return
    pre = 0
    for i in range(len(arr)):
        if v[i] == 0 and pre != arr[i]:
            choice.append(arr[i])
            v[i] = 1
            pre = arr[i]
            dfs()
            v[i] = 0
            choice.pop()

N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
choice = []
v = [0] * (N + 1)
dfs()
