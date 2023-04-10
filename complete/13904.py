n = int(input())
h = []
v = [0] * 1001 #
ans = 0
for i in range(n):
    s, e = map(int, input().split())
    h.append((s,e))
h.sort(key=lambda x:x[1], reverse=True) # 점수로 정렬하
for d, w in h:
    i = d
    while i > 0 and v[i] == 1:
        i -= 1
    if i == 0:
        continue
    else:
        v[i] = 1
        ans += w
print(ans)