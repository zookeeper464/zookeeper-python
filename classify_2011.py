s = "0" + input()
n = len(s)
dp = [1]*(n+1)
x=True
for i in range(1,n):
  if int(s[i-1]+s[i])==10 or int(s[i-1]+s[i])==20:
    dp[i+1]=dp[i-1]
  elif int(s[i-1]+s[i])%10==0:
    print(0)
    x=False
    break
  elif 10<int(s[i-1]+s[i])<27:
    dp[i+1]=(dp[i]+dp[i-1])%1000000
  else:
    dp[i+1]=dp[i]

if x:
  print(dp[-1])
