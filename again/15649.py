def dfs(n, lst):
    if n == M: # M개를 뽑아야 하므로 n == M 이 되었을 때
        ans.append(lst) # 정답리스트에 추가하고
        return # 함수 끝내기

    for j in range(1, N+1): # 1~N+1까지 숫자 묶는 경우의 수
        if v[j] == 0: # v로 중복처리 해주기
            v[j] = 1 # 중복처리 해주고
            dfs(n+1, lst+[j])
            v[j] = 0 # 함수 끝나면 다시 0으로 바꿔주기

N, M = map(int, input().split())
ans = []
v = [0] * (N+1) # 본인 숫자까지 방문처리 해야하니 N+1

dfs(0, [])
for lst in ans:
    print(*lst)

# def dfs(n,lst):
#     if n == M:
#         ans.append(lst)
#         return
#
#     for j in range(1, N+1):
#         if v[j] == 0:
#             v[j] = 1
#             dfs(n+1, lst+[j])
#             v[j] = 0
#
# N, M = map(int,input().split())
# ans = []
# v = [0] * (N+1)
# dfs(0,[])
# for lst in ans:
#     print(*lst)