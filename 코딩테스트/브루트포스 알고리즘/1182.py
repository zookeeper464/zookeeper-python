n,s = map(int,input().split())
lst = list(map(int,input().split()))
answer = 0

def dfs (cnt,temp,idx):
  global answer
  if temp == s and idx != -1:
    answer += 1
  
  if cnt == n:
    return
  
  for i in range(idx+1,n):
    temp += lst[i]
    dfs(cnt,temp,i)
    temp -= lst[i] 

dfs (0,0,-1)
print(answer)
