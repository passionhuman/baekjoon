st = input()
cnt = 0
ans = 0
for s in range(len(st)):
    if st[s] == '(':
        cnt += 1
    
    else:
        if st[s-1] == "(":
            cnt -= 1
            ans += cnt
        
        else:
            ans += 1
            cnt -= 1
print(ans)