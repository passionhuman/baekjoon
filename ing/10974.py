def permutation(arr, n):
    global chosen, v
    # 원소 담는 리스트에 원소를 저장하다가 n개가 되면 출력 후 함수 종료
    if len(chosen) == n:
        print(*chosen)
        return
    # 반복문을 돌리고
    for i in range(N):
        # 아직 사용하지 않았다면
        if not v[i]:
            # 선택리스트에 저장하고 방문체크한다.
            chosen.append(arr[i])
            v[i] = 1
            # 다시 generate 함수를 반복한다.
            permutation(arr, n)
            # 하나의 순열이 만들어지면 다시 방문체크를 0으로 돌려놓음
            v[i] = 0
            chosen.pop() # 원소 담은거 빼주기
import sys
N = int(sys.stdin.readline())
arr = [i for i in range(N+1)]
arr.pop(0)
chosen = []
v = [0 for _ in range(N+1)]
permutation(arr, N)