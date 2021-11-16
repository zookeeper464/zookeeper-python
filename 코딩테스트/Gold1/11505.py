n,m,k = map(int,input().split())
lst = [int(input()) for _ in range(n)]
dp = [0] * (4*n)
answer,zeros = [],set()
p = 1000000007

for i in range(lst):
  if lst[i] == 0:
    zeros.add(i)

def make (node,s,e):
  if s > e: dp[node] = 1; return 1
  elif s == e: dp[node] =  max(lst[s],1); return max(lst[s],1)

  mid = (s+e)//2
  temp = (make(node*2,s,mid)*make(node*2+1,mid+1,e))%p
  dp[node] = temp; return temp

def change (node,s,e,idx):
  global num
  if s > e:
    return

  dp[node] = ((dp[node]*max(lst[a],1))//max(1,num))%p
  mid = (s+e)//2

  if s==e: return
  elif idx>mid: change(node*2+1,mid+1,e,idx)
  else: change(node*2,s,mid,idx)

def check (node,l,r,s,e):
  if r<s or l>e:
    return 1
  elif s<=l and r<=e:
    return dp[node]
  
  mid = (l+r)//2
  temp = (check(node*2,l,mid,s,e)*check(node*2+1,mid+1,r,s,e))%p
  return temp

make(1,0,n-1)
for _ in range(m+k):
  x,a,b = map(int,input().split())
  a -= 1
  if x == 1:
    if b == 0:
      zeros.add(a)

    if lst[a] == 0:
      zeros -= {a}

    num,lst[a] = lst[a], b; change(1,0,n-1,a)

  else:
    if set(range(a,b+1))&zeros:
      answer.append(0)
      continue

    answer.append(check(1,0,n-1,a,b))

print(answer)
