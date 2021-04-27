from collections import deque

n = int(input())
lst = list(map(int,input().split()))
tree = [[] for _ in range(n)]
for idx, v in enumerate(lst):
  if v == -1:
    top = idx
  else:
    tree[v].append(idx)
#나무구조와 뿌리를 설정해준다.

t = int(input())
q = deque([t])
#빼야하는 노드를 설정한다.

cnt = 0
#빠지는 뿌리
while q:
  temp = q.popleft()
  if tree[temp] != []:
    for i in tree[temp]:
      q.append(i)
      #만약 temp가 뿌리가 아니라면 뿌리를 찾기 위한 노드들을 q에 넣는다.
  else:
    cnt += 1
    #만약 temp가 뿌리였다면 빼야하는 수를 늘린다.

answer = tree.count([]) - cnt + tree.count([t])
print(answer)
