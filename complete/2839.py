n = int(input())
five = n // 5
check = True
while check:
    if n % 5 == 0:
        print(five)
        break
    else:
        while True:
            temp = n - (five * 5)
            if temp % 3 == 0:
                three = temp // 3
                print(three + five)
                check = False
                break
            five -= 1
            if five < 0:
                check = False
                print(-1)
                break