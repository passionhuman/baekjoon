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
