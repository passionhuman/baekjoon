import sys
st = sys.stdin.readline().rstrip()
boom = sys.stdin.readline().rstrip()
stack = []

for s in st:
    stack.append(s)
    if s == boom[-1] and ''.join(stack[len(stack)-len(boom):]) == boom:
        for i in range(len(boom)):
            stack.pop()
if stack:
    print(''.join(stack))
else:
    print("FRULA")