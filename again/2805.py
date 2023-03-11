import sys
n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
start = 1
end = max(lst)
while start <= end:
    mid = (start + end) // 2
    tree = 0
    for i in range(len(lst)):
        if lst[i] > mid:
            tree += lst[i] - mid
    if tree >= m:
        start = mid + 1
    elif tree < m:
        end = mid - 1
print(end)