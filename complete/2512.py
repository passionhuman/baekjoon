n = int(input())
lst = list(map(int, input().split()))
m = int(input())
end = max(lst)
start = 1
ans = 0
while start <= end:
    sum_num = 0
    mid = (start + end) // 2
    for i in range(len(lst)):
        if lst[i] > mid:
            sum_num += mid
        else:
            sum_num += lst[i]
    if sum_num > m:
        end = mid - 1
    else:
        if sum_num <= m:
            ans = mid
            start = mid + 1
        else:
            start = mid + 1
print(ans)