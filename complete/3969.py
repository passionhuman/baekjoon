n = int(input())
cnt = 0
for _ in range(n):
    stack = []
    st = input()
    check = True
    temp = ''
    for i in st:
        if i == 'A' and not stack:
            stack.append('A')
        
        elif i == 'B' and not stack:
            stack.append('B')
        
        elif i == 'A':
            temp = stack.pop()
            if temp == 'A':
                pass
            else:
                stack.append(temp)
                stack.append('A')
                
        
        elif i == 'B':
            temp = stack.pop()
            if temp == 'B':
                pass
            else:
                stack.append(temp)
                stack.append('B')
       

    if stack:
        check = False

    elif not stack and check == True:
        cnt += 1
        
    
print(cnt)

