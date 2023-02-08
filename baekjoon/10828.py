import sys

stack = [] # 스택생성
N = int(input()) 
for i in range(N): # 문자열 입력을 빠르게 받기 위해 sys 사용
    command = list(map(str, sys.stdin.readline().rstrip().split())) # list로 만들어 첫번째는 명령어, 두 번째는 숫자입력
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