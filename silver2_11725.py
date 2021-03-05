from collections import deque
import sys
input=sys.stdin.readline

N=int(input())
e_lst=list([[] for i in range(N+1)])
v_lst=[0]*(N+1)
v_lst[1]=1
for i in range(N-1):
  a,b=map(int,input().split())
  e_lst[a].append(b)
  e_lst[b].append(a)


q=deque()
q.append(1)
while q:
  temp=q.popleft()
  for i in e_lst[temp]:
    if v_lst[i]==0:
      q.append(i)
      v_lst[i]=v_lst[temp]+1

for i in range(2,N+1):
  for j in e_lst[i]:
    if v_lst[i]==v_lst[j]+1:
      print(j)
