n,k = map(int,input().split())
wlst, vlst = [], []
for i in range(n):
  w,v = map(int,input().split())
  wlst.append(w)
  vlst.append(v)

dp = [0 for _ in range(k+1)]
for i in range(1,k+1):
  for j in range(n):
    if i>=wlst[j] and dp[i-wlst[j]]+vlst[j]>dp[i]:
      dp[i] = dp[i-wlst[j]]+vlst[j]

print(max(dp))
