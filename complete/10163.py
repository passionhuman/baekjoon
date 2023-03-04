n = int(input())
arr = [[0] * 1001 for _ in range(1001)]
temp = 1
ans = 0
remove_set = {0}
result = []
for _ in range(n):
    b, a, c, r = map(int, input().split())
    for i in range(r):
        for j in range(c):
            arr[a+i][b+j] = temp
    temp += 1

for k in range(1, n+1):
    ans = result.count(k)
    print(ans)