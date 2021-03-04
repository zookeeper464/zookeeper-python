from collections import deque
import sys
input=sys.stdin.readline

q=deque()
N=int(input())
start, end = map(int,input().split())
M=int(input())
m_lst=list([[] for i in range(101)])
n_lst=[-1]*101
for i in range(M):
  a,b = map(int,input().split())
  m_lst[a].append(b)
  m_lst[b].append(a)

n_lst[start]=0
q.append(start)
while q:
  x=q.popleft()
  for i in m_lst[x]:
    if n_lst[i]==-1:
      q.append(i)
      n_lst[i]=n_lst[x]+1
  
print(n_lst[end])
