n = int(input())
lst = []
for i in range(n):
    age, m = input().split()
    lst.append([int(age), m])
lst.sort(key=lambda x:x[0])
for i in range(n):
    print(*lst[i])