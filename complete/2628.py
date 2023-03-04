r_list = [0]
c_list = [0]
c, r = map(int, input().split())
r_list.append(r)
c_list.append(c)
r_max = c_max = 0
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    if a == 0:
        r_list.append(b)
    else:
        c_list.append(b)
r_list = sorted(r_list,reverse=True)
c_list = sorted(c_list,reverse=True)
for r in range(len(r_list)-1):
    temp = r_list[r] - r_list[r+1]
    if temp > r_max:
        r_max = temp
for c in range(len(c_list)-1):
    temp = c_list[c] - c_list[c+1]
    if temp > c_max:
        c_max = temp
print(r_max * c_max)