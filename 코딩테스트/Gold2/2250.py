from collections import deque

class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None
    self.index = None
    self.state = None

def dfs(num):
  global answer,idx
  if N_list[num].left != -1:
    dfs(N_list[num].left)

  N_list[num].index = idx
  temp = N_list[num].state
  check[temp][0] = min(check[temp][0],idx)
  check[temp][1] = max(check[temp][1],idx)
  idx += 1

  if N_list[num].right != -1:
    dfs(N_list[num].right)

N = int(input())
N_list = [Node(i) for i in range(N+1)]
st = set(range(1,N+1))

for _ in range(N):
  d,l,r = map(int,input().split())
  N_list[d].left = l
  N_list[d].right = r
  st -= {l}
  st -= {r}

start = list(st)[0]
q = deque([start])
num = 1
while q:
  for _ in range(len(q)):
    temp = q.popleft()
    N_list[temp].state = num
    if N_list[temp].left != -1:
      q.append(N_list[temp].left)
    if N_list[temp].right != -1:
      q.append(N_list[temp].right)
  
  num += 1
  
check = [[N,0] for _ in range(num)]
answer,idx = 0,1

dfs(start)
for i,(a,b) in enumerate(check):
  if answer >= b-a+1:
    continue
  answer = b-a+1
  idx = i

print(idx,answer)
