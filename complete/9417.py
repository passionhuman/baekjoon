T = int(input())
for i in range(T):
    num_list = list(map(int, input().split()))
    num_list = sorted(num_list)
    temp = 0
    max_num = 0
    for i in range(len(num_list) - 1):
        for j in range(i + 1, len(num_list)):
            temp = num_list[i]
            while temp > 1:
                if num_list[j] % temp == 0 and num_list[i] % temp == 0:
                    if max_num < temp:
                        max_num = temp
                    break
                else:
                    temp -= 1

    if max_num == 0:
        print(1)
    else:
        print(max_num)
