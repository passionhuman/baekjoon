n = int(input())
lst = input().split()
cnt = 0
for i in range(n-1, 0, -1):
    for j in range(i):
        if int(lst[j] + lst[j+1]) > int(lst[j+1] + lst[j]):
            pass
        else:
            lst[j], lst[j+1] = lst[j+1], lst[j]

for l in lst:
    if l == "0":
        cnt += 1

if cnt == n:
    print(0)
else:
    print(''.join(lst))