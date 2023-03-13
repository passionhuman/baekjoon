import sys
st = sys.stdin.readline().rstrip()
find = sys.stdin.readline().rstrip()
stack = []
cnt = 0
for i in st:
    stack.append(i) # stack에 문자열 하나씩 넣어주고
    if i == find[-1]: # 끝 문자열과 들어오는 문자열이 같다면
        if "".join(stack[-len(find):]) == find: # 끝기준으로 find 길이만큼 비교
            stack = [] # 스택 비워주기
            cnt += 1 # 비교 문자열이 한 번 검색된 거므로 답 +1
print(cnt)