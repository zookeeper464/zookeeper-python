n,h = map(int,input().split())
dic = [0]*(h+1)
dic[h] = n//2
for _ in range(n//2):
  up = int(input())
  down = h - int(input())
  dic[up] += 1
  dic[down] -= 1

dp = [0]*(h+1)
dp[-1] = dic[h]
for i in range(h-1,0,-1):
  dp[i] = dic[i]+dp[i+1]

num = n
cnt = 0
for i in range(1,h+1):
  if num < dp[i]:
    continue

  if num == dp[i]:
    cnt += 1
  
  else:
    num = dp[i]
    cnt = 1

print(num,cnt)