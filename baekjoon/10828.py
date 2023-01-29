import sys


stack = []
N = int(input())


for i in range(N):
    command = list(map(str, sys.stdin.readline().rstrip().split()))
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        if not stack:
            print(-1)
        else:
            temp = stack.pop()
            print(temp)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if not stack:
            print(1)
        elif stack:
            print(0)
    elif command[0] == "top":
        if stack:
            print(stack[-1])
        elif not stack:
            print(-1)