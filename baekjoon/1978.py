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