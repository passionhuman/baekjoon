k = int(input())
num_list = []
num_sum = 0
for i in range(k): # k번까지 돌음
    num = int(input())
    if num != 0: # 들어오는 수가 0이 아니면 리스트에 추가
        num_list.append(num)
    elif num == 0: # 0이 들어오면 pop 하여 빼주기
        num_list.pop()
for i in num_list: # 리스트안의 원소들 빼서 다 더해주기
    num_sum += i
print(num_sum) # 모든 원소들의 합 출력