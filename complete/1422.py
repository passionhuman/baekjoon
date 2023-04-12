k, n = map(int, input().split())
lst = []
for _ in range(k):
    temp = int(input())
    lst.append(temp) # int형으로 다 저장해주고
max_num = max(lst) # 제일 큰 숫자 max_num에 저장
temp_num = n-k # 제일 큰 숫자를 n-k번 더 써야하므로 temp_num에 저장
for i in range(temp_num): # lst에 temp_num 만큼 max_num 추가해주기
    lst.append(max_num)
for i in range(len(lst)-1,0,-1): # 버블정렬
    for j in range(i): # 문자열로 붙여보고 더 큰 숫자가 만들어지면 자리바꿈
        if int(str(lst[j])+str(lst[j+1])) < int(str(lst[j+1])+str(lst[j])):
            lst[j], lst[j+1] = lst[j+1], lst[j]
for i in lst:
    print(i,end="") # 붙여서 출력