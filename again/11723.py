import sys
m = int(sys.stdin.readline())
bit = num = 0
for _ in range(m):
    st = list(sys.stdin.readline().split())
    oper = st[0]
    if len(st) == 2:
        num = st[1]
    num = int(num)
    if oper == "add":
       bit |= (1 << num)
    elif oper == "remove":
        bit &= ~(1 << num)
    elif oper == "check":
        if bit & (1 << num) > 0:
            print(1)
        else:
            print(0)
    elif oper == "toggle":
        bit ^= (1 << num)
    elif oper == "all":
        bit = (1 << 21) - 1
    else:
        bit = 0
