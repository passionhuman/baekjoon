import sys
ans = []
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
order = [1] * n
for i in range(n):
    for j in range(i):
        if lst[i] < lst[j] and order[i] <= order[j]:
            order[i] = order[j] + 1
print(max(order))