N = int(input())
ans = 0
for i in range(7):
    if N & (1<<i):
        ans += 1
print(ans)


