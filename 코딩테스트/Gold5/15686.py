n,m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
home,chichi = [], []
answer = 1000000
for r in range(n):
  for c in range(n):
    if lst[r][c] == 1:
      home.append((r,c))
    elif lst[r][c] == 2:
      chichi.append((r,c))
h,ch = len(home),len(chichi)

def check(temp):
  global answer
  cnt = 0
  for y,x in home:
    num = 100
    for i in temp:
      r,c = chichi[i]
      num = min(num, abs(y-r)+abs(x-c))
    cnt += num

  answer = min(answer,cnt)

def dfs (cnt,idx,temp):
  if cnt == m:
    check(temp)
    return

  for i in range(idx+1,ch):
    temp.append(i)
    dfs(cnt+1,i,temp)
    temp.pop()

dfs(0,-1,[])
print(answer) 
