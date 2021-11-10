import sys
inf = sys.maxsize

def min_init (node,start,end):
  if start == end:
    min_dp[node] = lst[start]
    return min_dp[node]

  mid = (start+end)//2
  
  min_dp[node] = min(min_init(node*2,start,mid),min_init(node*2+1,mid+1,end))
  return min_dp[node]

def min_check (start,end,node,s,e):
  if s > end or e < start:
      return inf

  if s <= start and end <= e:
      return min_dp[node]

  mid = (start + end) // 2
  mi = min(min_check(start,mid,node*2,s,e),min_check(mid+1,end,node*2+1,s,e))
  return mi

def max_init (node,start,end):
  if start == end:
    max_dp[node] = lst[start]
    return max_dp[node]

  mid = (start+end)//2
  
  max_dp[node] = max(max_init(node*2,start,mid),max_init(node*2+1,mid+1,end))
  return max_dp[node]

def max_check (start,end,node,s,e):
  if s > end or e < start:
      return -inf

  if s <= start and end <= e:
      return max_dp[node]

  mid = (start + end) // 2
  mx  = max(max_check(start,mid,node*2,s,e),max_check(mid+1,end,node*2+1,s,e))
  return mx

N,M = map(int,input().split())
lst = [int(input()) for _ in range(N)]
min_dp, max_dp = [0] *(4*N), [0] *(4*N)
min_init(1,0,N-1)
max_init(1,0,N-1)
answer = []

for _ in range(M):
  a,b = map(int,input().split())
  mi = min_check(0,N-1,1,a-1,b-1)
  mx = max_check(0,N-1,1,a-1,b-1)
  answer.append(f'{mi} {mx}')

print('\n'.join(answer))
