n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
dp = [[] for _ in range(n-1)]
for i in range(n-1):
  for j in range(i+1,n):
    dp[i].append(lst[i][j]+lst[j][i])
answer = 20000

def cal (lst):
  temp = 0
  for i in range(n//2-1):
    for j in range(i+1,n//2):
      temp += dp[lst[i]][lst[j]-lst[i]-1]
  return temp

def check(lst1):
  global answer
  lst2 = []
  for i in range(n):
    if i not in lst1:
      lst2.append(i)
  
  x = abs(cal(lst1)-cal(lst2))
  if answer > x:
    answer = x

def dfs (cnt,lst):
  if cnt == n//2:
    check(lst)
    return
  for i in range(lst[-1]+1,n-1):
    lst.append(i)
    dfs(cnt+1,lst)
    lst.pop()

for i in range(n//2):
  dfs(1,[i])

print(answer)
