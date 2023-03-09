n = int(input())
lst = list(map(int, input().split()))
a = 0
b = n-1
cnt = 0
minV = 20000000000
while a != b:
    temp = lst[a] + lst[b]
    if abs(temp) < minV:
        minV = abs(temp)
        ans_s = lst[a]
        ans_e = lst[b]
        if minV == 0:
            break
    if temp > 0:
        b -= 1
    elif temp < 0:
        a += 1
print(ans_s, ans_e)