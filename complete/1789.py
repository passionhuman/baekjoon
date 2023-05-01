num = int(input())
N = 0
result = 0
for i in range(1,num+1):
    result += i
    N += 1
    if(result > num):
        N -= 1
        break;
print(N)