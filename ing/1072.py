x, y = map(int, input().split())
ans = int(y * 100 / x)
s = 1
e = x
res = []
while s <= e:
    mid = (s + e) // 2
    temp = int(y*100 / (x + mid))
    if ans != temp:
        e = mid -1
        res.append(mid)
    else:
        s = mid + 1
print(res)
