pre_order = [] # 전위
in_order = [] # 중위
post_order = [] # 후위
tree = {} # tree 딕셔너리
n = int(input()) # 노드의 개수 입력받기
for i in range(n):
    r, left, right = list(map(str, input().split())) # 루트, 왼쪽자식, 오른쪽자식
    if left == '.': # 왼쪽자식이 없으면 0으로 받기
        left = 0
    if right == '.': # 오른쪽자식이 없으면 0으로 받기
        right = 0
    tree[r] = [left, right]

def preorder(t): # 전위순회
    if tree[t]: # 시작노드의 값이 있으면
        pre_order.append(t) # 전위순회 출력하기위한 pre_order에 추가
        if tree[t][0]: # 왼쪽자식이 있으면
            preorder(tree[t][0]) # 다시 함수 돌리기

        if tree[t][1]: # 오른쪽자식 있으면
            preorder(tree[t][1]) # 함수 돌리기

def inorder(t): # 중위순회
    if tree[t]: # 시작노드의 값이 있으면
        if tree[t][0]: # 왼쪽 자식이 있으면
            inorder(tree[t][0]) # 함수 돌리기
        in_order.append(t) # 그 다음 출력하기 위한 배열에 담고
        if tree[t][1]: # 오른쪽 자식 있으면
            inorder(tree[t][1]) # 함수 돌리기

def postorder(t):
    if tree[t]: # 값이 있으면
        if tree[t][0]: # 왼쪽 자식 있으면
            postorder(tree[t][0]) # 함수 돌리고
        if tree[t][1]: # 오른쪽 자식 있으면
            postorder(tree[t][1]) # 함수 돌리기
        post_order.append(t) # 출력위한 배열에 담기
preorder('A')
inorder('A')
postorder('A')
for i in pre_order:
    print(i, end = '')
print()
for i in in_order:
    print(i, end = '')
print()
for i in post_order:
    print(i, end = '')