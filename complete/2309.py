stack = []
ans = []
result = []
for i in range(9):
    num = int(input())
    stack.append(num) # num이라는 배열에 입력값 받기

for i in range(9): # 9가지 중 2가지 수를 빼서 나머지 들의 합이 100이 되는지 확인
    for j in range(9):
        if i == j: # 같은 수를 뺄 때는 continue로 건너뛰기
            continue
        temp_i = stack[i] # 임시 변수에 받아두기
        temp_j = stack[j]
        stack[i] = 0
        stack[j] = 0
        if sum(stack) == 100: # 나머지 수들의 합이 100이 될 경우
            ans.append(i) # 두 개의 값을 ans 리스트에 넣어놓고
            ans.append(j)
        else:
            stack[i] = temp_i # 다시 그 자리에 넣기
            stack[j] = temp_j

stack[ans[0]] = 0 # 스택에 빼야 되는 수 2개를 넣기
stack[ans[1]] = 0
for s in stack:
    if s != 0:
        result.append(s) # 빼야되는 수들을 빼고 정답 리스트에 넣고 출력
result = sorted(result)
for s in result:
    print(s)