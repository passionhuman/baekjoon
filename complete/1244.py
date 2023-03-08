switch_num = int(input())
switch = list(map(int, input().split()))
n = int(input())
for _ in range(n):
    gen, num = map(int,input().split())
    temp = num
    if gen == 1:
        while num <= switch_num:
            if switch[num-1] == 1:
                switch[num-1] = 0
            elif switch[num-1] == 0:
                switch[num-1] = 1
            num += temp
    else:
        if switch[num-1] == 1:
            switch[num-1] = 0
        elif switch[num - 1] == 0:
            switch[num - 1] = 1
        s = num - 2
        e = num
        while True:
            if s >= 0 and e < switch_num and switch[s] == switch[e]:
                if switch[s] == 1:
                    switch[s] = 0
                    switch[e] = 0
                else:
                    switch[s] = 1
                    switch[e] = 1
            else:
                break
            s -= 1
            e += 1
for i in range(len(switch)):
    if i != 0 and i % 20 == 0:
        print()
    print(switch[i], end = " ")