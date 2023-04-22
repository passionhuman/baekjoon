lst = [0] * 10
ans = 0
st = input()
for s in st:
    if s == "6" and lst[6] == 0 and lst[9] > 0:
        lst[9] -= 1

    elif s =="9" and lst[9] == 0 and lst[6] > 0:
        lst[6] -= 1


    elif lst[int(s)] == 0:
        ans += 1
        for i in range(len(lst)):
            lst[i] += 1
        lst[int(s)] -= 1

    elif lst[int(s)] > 0:
        lst[int(s)] -= 1
print(ans)