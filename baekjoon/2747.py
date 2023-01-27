# 내가 n 번째의 피보나치 수를 얻기 위해서는
# n - 1 번째와 n - 2번째 수만 알면됨
# 그렇다면 n - 1 번째까지 피보나치 수를 리스트에 넣고
# n - 1 과 n - 2 의 피보나치 수를 더하자

# 단순한 for문 이용하여 풀어보기
n = int(input())
result = [0, 1]


for i in range(n - 1):
    temp = result[i] + result[i + 1]
    result.append(temp)

# print(result[-1])

# 재귀함수로 풀어보기
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

N = int(input())
print(fibonacci(N))