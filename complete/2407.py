n, m = map(int, input().split())
n_temp = 1
m_temp = 1
for i in range(m):
    n_temp *= n
    n -= 1
for i in range(2, m+1):
    m_temp *= i
print(n_temp // m_temp)