from collections import deque

n,m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
chicken,home,answer = [], [], 10000
dr,dc = [1,-1,0,0],[0,0,-1,1]
for r in range(n):
  for c in range(n):
    if lst[r][c] == 2:
      chicken.append([r,c])
    elif lst[r][c] == 1:
      home.append([r,c])

c = len(chicken)

def check (q):
  ans = 0
  for i,j in home:
    temp = 100
    for x,y in q:
      temp = min(temp,abs(i-x)+abs(j-y))
    ans += temp
  return ans


def dfs (cnt,num,q):
  global answer
  if cnt == m:
    x = check(q)
    if answer > x: 
      answer = x
    return
  
  for i in range(num+1,c):
    q.append(chicken[i])
    dfs(cnt+1,i,q)
    q.pop()

dfs(0,-1,[])
print(answer)
