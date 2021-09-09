t = int(input())
l = []

for _ in range(t):
  n = int(input())
  dp = [0] * (n+1)
  for _ in range(n):
    a,b = map(int,input().split())
    dp[a] = b
  temp, cnt = n+1, 0
  for b in range(1,n+1):
    if dp[b] < temp:
      cnt += 1
      temp = dp[b]
  
  l.append(cnt)

print(*l, sep='\n')
