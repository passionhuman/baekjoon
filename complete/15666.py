def dfs():
    if len(choice) == M:
        temp = choice[0] # 선택된 첫 번째 수 기준으로 잡고
        for i in range(M):
            if temp > choice[i]: # 만약 비내림차순이 아니면 
                return # 바로 리턴
            else:
                temp = choice[i]  # 그 다음 순자로 기준 숫자를 변경
        print(*choice) # 비내림차순이면 선택 원소들 출력
        return
    pre = 0 # 최근에 선택한 원소 저장한기위한 변수
    for i in range(len(arr)): # 같은 수를 골라도 되므로 방문체크 x
        if pre != arr[i]: # 최근에 선택한 원소랑 같지 않으면 (중복 순열 출력하지 않기 위해)
            choice.append(arr[i]) # 선택 원소 추가해주고
            pre = arr[i] # pre를 선택한 숫자로 최신화 해주고
            dfs() # 다시 함수 호출
            choice.pop() # 함수가 끝나면 선택원소에서 빼주기

N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
choice = []
dfs()
