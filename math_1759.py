l,c=map(int,input().split())
lst=input().split()
lst.sort()
visited=[False]*c
answer=[]
sol=["a","e","i","o","u"]

def dfs (depth,j):
  if depth ==l:
    if 0<len(set(answer)&set(sol))<l-1:
      print("".join(map(str,answer)))
      return
  
  for i,v in enumerate(lst):
    if not visited[i] and i>j:
      visited[i]=True
      answer.append(v)
      dfs(depth+1,i)
      visited[i]=False
      answer.pop()

dfs(0,-1)
