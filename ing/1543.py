import sys
from collections import deque
st = sys.stdin.readline().rstrip()
find = sys.stdin.readline().rstrip()
q = deque([])
cnt = 0
for i in range(len(st)):
    q.append(st[i])

for i in range(len(q)):
    if i >= len(q):
        break
        if st[i:i+len(find)] == find:
            cnt += 1
            for j in range(len(find)):
                q.pop(i)
print(q)
