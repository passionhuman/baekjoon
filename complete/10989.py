import sys
n = int(sys.stdin.readline())
lst = [0] * 10001
for _ in range(n):
    temp = int(sys.stdin.readline())
    lst[temp] += 1
for i in range(len(lst)):
    if lst[i] > 0:
        for j in range(lst[i]):
            print(i)