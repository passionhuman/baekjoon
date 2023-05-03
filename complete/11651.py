import sys
n = int(sys.stdin.readline())
result = []
for i in range(n):
    result.append(list(map(int, sys.stdin.readline().split())))
result.sort(key=lambda x: (x[1], x[0]))
for i in result:
    print(i[0], i[1])