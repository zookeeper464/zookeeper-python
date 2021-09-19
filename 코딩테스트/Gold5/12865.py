n,k=map(int,input().split())
dp=[0]*(k+1)
w=[]
v=[]
for i in range(n):
  w_,v_=map(int, input().split())
  w.append(w_)
  v.append(v_)

for i in range(n):
  for j in range(k,0,-1):
    if j-w[i]>=0:
      dp[j]=max(dp[j],v[i]+dp[j-w[i]])
  
print(max(dp))
