n = int(input())
prime_list = [True] * (n + 1)
m = int(n ** 0.5)

for i in range(2, m + 1):
    if prime_list[i] == True:
        for j in range(i + i, n + 1, i):
            prime_list[j] = False

for i in range(2, n + 1):
    if prime_list[i] == True:
        print(i)
=======
N = int(input())
Num_list =sorted(list(map(int, input().split())))
prime = [True] * (Num_list[-1] + 1)
prime[0] = False
prime[1] = False
result = []

for i in range(2, int((Num_list[-1]) ** 0.5) + 1):
    if prime[i]:
        for j in range(i * 2, Num_list[-1] + 1, i):
            prime[j] = False

for i in range(Num_list[-1]+1):
    if prime[i]:
        if i in Num_list:
            result.append(i)

print(len(result))
