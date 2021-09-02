n,m = map(int,input().split())
lst = input().split()
lst.sort()

def dfs (cnt1,cnt2,num,s):
  if cnt1+cnt2 == n:
    if cnt1>0 and cnt2>1:
      print(s)
    return
  for i in range(num+1,m):
    if lst[i] in 'aeiou':
      dfs(cnt1+1,cnt2,i,s+lst[i])
    else:
      dfs(cnt1,cnt2+1,i,s+lst[i])

for i in range(m-n+1):
  if lst[i] in 'aeiou':
    dfs(1,0,i,lst[i])
  else:
    dfs(0,1,i,lst[i])
