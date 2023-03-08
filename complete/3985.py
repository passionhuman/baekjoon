l = int(input())
lst = [0] * (l + 1)
n = int(input())
max_count = 0
expect = 0
for i in range(1, n+1):
    s, e = map(int, input().split())
    if e-s > expect:
        expect = e-s
        expecter = i
    for j in range(s,e+1):
        if lst[j] == 0:
            lst[j] = i

for i in range(1,n+1):
    temp = lst.count(i)
    if temp > max_count:
        max_count = temp
        max_counter = i
print(expecter)
print(max_counter)