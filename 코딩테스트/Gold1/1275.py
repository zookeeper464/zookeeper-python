def make (node,s,e):
    if s==e:
        dp[node] = lst[s]
        return dp[node]

    mid = (s+e)//2
    dp[node] = make(node*2,s,mid)+make(node*2+1,mid+1,e)
    return dp[node]

def check(node,l,r,x,y):
    if r<x or y<l or l>r:
        return 0
    
    if x<=l<=r<=y:
        return dp[node]
    
    mid = (l+r)//2
    temp = check(node*2,l,mid,x,y)+check(node*2+1,mid+1,r,x,y)
    return temp

def update(node,l,r,a,b):
    if r<a or a<l or l>r:
        return 
    if l==r and l==a:
        dp[node] = b
        return

    mid = (l+r)//2
    update(node*2,l,mid,a,b)
    update(node*2+1,mid+1,r,a,b)

    if l<=a<=r:
        dp[node] += b-lst[a]
    
n,m = map(int,input().split())
lst = list(map(int,input().split()))
dp = [0] *(4*n)
make(1,0,n-1)
answer = []

for _ in range(m):
    x,y,a,b = map(int,input().split())
    if x<y: temp = check(1,0,n-1,x-1,y-1)
    else: temp = check(1,0,n-1,y-1,x-1)
    update(1,0,n-1,a-1,b)
    lst[a-1] = b
    answer.append(temp)

print(*answer,sep='\n')