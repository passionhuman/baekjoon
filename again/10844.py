N = int(input())
lst = [[0]*12 for _ in range(N+1)]
lst[1][2:11] = [1] * 9
for i in range(2, N+1):
    for j in range(1,11):
        lst[i][j] = lst[i-1][j-1]+lst[i-1][j+1]
ans = sum(lst[N])
print(ans%1000000000)