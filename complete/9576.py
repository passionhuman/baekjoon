t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    book = [list(map(int, input().split())) for _ in range(m)]
    book.sort(key= lambda x:x[0])
    book.sort(key= lambda x:x[1])
    v = [0] * (n + 1)
    ans = 0
    for a, b in book:
        for i in range(a,b+1):
            if v[i] == 0:
                ans += 1
                v[i] = 1
                break
            elif v[i] == 0:
                ans += 1
                v[i] = 1
                break
        if ans == n:
            break
    print(ans)