from sys import stdin

def input():
  return stdin.readline().rstrip('\n')

N = int(input())
tree = {}

for _ in range(N):
  node,left,right = input().split(" ")
  tree[node] = [left,right]

def preOrder(node):
  if node == '.': return

  answer.append(node)
  preOrder(tree[node][0])
  preOrder(tree[node][1])

def inOrder(node):
  if node == '.': return

  inOrder(tree[node][0])
  answer.append(node)
  inOrder(tree[node][1])

def postOrder(node):
  if node == '.': return

  postOrder(tree[node][0])
  postOrder(tree[node][1])
  answer.append(node)

answer = []
preOrder('A')
print("".join(answer))
answer = []
inOrder('A')
print("".join(answer))
answer = []
postOrder('A')
print("".join(answer))
