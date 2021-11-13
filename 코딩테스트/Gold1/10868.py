import sys
inf = sys.maxsize

def dfs(idx,a,b):
  if a >= b:
    dp[idx] = lst[a]
    return dp[idx]

  temp = (a+b)//2
  dp[idx] = min(dfs(2*idx,a,temp),dfs(2*idx+1,temp+1,b))
  return dp[idx]

def check(idx,l_idx,r_idx):
  global a,b
  if (b < l_idx or a > r_idx) or l_idx>r_idx:
    return inf

  if a <= l_idx and b >= r_idx:
    return dp[idx]

  m_idx = (l_idx+r_idx)//2
  num = min(check(idx*2,l_idx,m_idx),check(idx*2+1,m_idx+1,r_idx))
  return num

n,m = map(int,input().split())
lst = [int(input()) for _ in range(n)]
dp = [inf for _ in range(4*n)]
dfs(1,0,n-1)
answer = []

for _ in range(m):
  a,b = map(int,input().split())
  a,b = a-1,b-1
  answer.append(check(1,0,n-1))

print(*answer,sep='\n')
