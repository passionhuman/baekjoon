import sys


stack = [] # 리스트라는 스택생성
N = int(input())

for i in range(N): # 입력받은 N번의 횟수 돌고
    command = list(map(str, sys.stdin.readline().rstrip().split())) # 입력을 여러번 받으므로 Sys 사용하여 시간초과 안 나게
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