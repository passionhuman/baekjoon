import sys
stack = []
max_n = 0
temp = 0
cnt = 0
n = int(sys.stdin.readline)
for _ in range(n):
    num = int(sys.stdin.readline)
    stack.append(num)

for i in range(len(stack)):
    temp = stack.pop()
    if temp > max_n:
        cnt += 1
        max_n = temp

print(cnt)