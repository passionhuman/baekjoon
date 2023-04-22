n, k = map(int, input().split())
ans = 0
while True:
    one_cnt = bin(n).count("1")
    if one_cnt > k:
        n += 1
        ans += 1
    else:
        break
print(ans)