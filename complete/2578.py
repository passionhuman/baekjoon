arr = [list(map(int, input().split())) for _ in range(5)]
bing = [list(map(int, input().split())) for _ in range(5)]
cnt = 0
result = 25
for i in range(5):
    for j in range(5):
        temp = bing[i][j]
        for r in range(5):
            for c in range(5):
                if arr[r][c] == temp:
                    arr[r][c] = 0
                    cnt += 1
                    break
        if cnt >= 12:
            check = 0
            for a in arr:
                temp = a.count(0)
                if temp == 5:
                    check += 1
            for coloum in range(5):
                temp_cnt = 0
                for row in range(5):
                    if arr[row][coloum] == 0:
                        temp_cnt += 1
                if temp_cnt == 5:
                    check += 1

            temp_cnt = 0
            for row in range(5):
                for col in range(row, row+1):
                    if arr[row][col] == 0:
                        temp_cnt += 1
            if temp_cnt == 5:
                check += 1

            temp_cnt = 0
            for row in range(5):
                for col in range(4-row,5-row):
                    if arr[row][col] == 0:
                        temp_cnt += 1
            if temp_cnt == 5:
                check += 1

            if check >= 3:
                if cnt < result:
                    result = cnt
print(result)