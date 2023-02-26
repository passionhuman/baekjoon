import sys
# sys 이용하여 입력시간 줄이고
st = sys.stdin.readline().rstrip()
re_st = sorted(st, reverse=True) # sorted와 reverse 이용하여 내림차순 정렬
print(''.join(re_st)) # join 이용하여 문자열로 출력