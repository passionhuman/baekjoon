n = int(input())

for _ in range(2):
    inorder = map(int, input().split())
    postorder = map(int, input().split())
root = postorder[-1]

