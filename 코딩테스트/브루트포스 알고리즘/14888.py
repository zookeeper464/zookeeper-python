n = int(input())
lst = list(map(int,input().split()))
p,m,mul,div = map(int,input().split())
mx = -10**9
mi = 10**9

def dfs (num,p,m,mul,div,result):
  global mx,mi
  if num == n:
    if mx < result:
      mx = result 
    if mi > result:
      mi = result
    return
  
  if p:
    dfs (num+1,p-1,m,mul,div,result+lst[num])
  if m:
    dfs (num+1,p,m-1,mul,div,result-lst[num])
  if mul:
    dfs (num+1,p,m,mul-1,div,result*lst[num])
  if div:
    if result >= 0:
      dfs (num+1,p,m,mul,div-1,result//lst[num])
    else:
      dfs (num+1,p,m,mul,div-1,-(-result//lst[num]))

dfs(1,p,m,mul,div,lst[0])
print(mx,mi,sep='\n')
