n = int(input())
lst = []
ans = []
result = []
for i in range(n):
    a, b = map(int,input().split())
    lst.append([a,b])

def combi(cnt,ans):
    if cnt == n:
        if ans:
            mul_ = 1
            add_ = 0
            for a in ans:
                mul_ *= a[0]
                add_ += a[1]
            result.append(abs(mul_ - add_))
        return


    ans.append(lst[cnt])
    combi(cnt+1, ans)
    ans.pop()
    combi(cnt+1, ans)

combi(0,[])
print(min(result))

2 3 4