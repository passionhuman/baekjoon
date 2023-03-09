k, n = map(int, input().split())
stack = []
ans = []
for i in range(k):
    temp = int(input())
    stack.append(temp)
stack.sort()
s = 1
e = stack[-1]
cnt = 0

while s <= e:
    mid = (s + e) // 2
    for i in range(len(stack)):
        cnt += stack[i] // mid
    if cnt >= n:
        ans.append(mid)

    if cnt < n:
        e = mid - 1

    elif cnt >= n:
        s = mid + 1
    cnt = 0
print(max(ans))