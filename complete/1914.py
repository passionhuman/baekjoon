# n 으로 입력값 받기
n = int(input())

# n = 움직여야하는 원판의 개수, m 차례대로 1, 2, 3
def hanoi(n, m1, m3, m2):
    
    
    if n == 1:
        print(m1, m3)
    else:
        hanoi(n-1, m1, m2, m3) # n-1 개를 m1에서 m2로 이동 (m3 보조기둥)
        print(m1, m3) # n 번째 원판을 m1 -> m3 이동
        hanoi(n-1, m2, m3, m1) # 옮겨진 n-1개 원판을 m2에서 m3로 이동(m1 보조기둥)


print(2 ** n - 1)
if n <= 20:
    hanoi(n, 1, 3, 2)