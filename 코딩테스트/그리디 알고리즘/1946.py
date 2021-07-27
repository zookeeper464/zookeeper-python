t = int(input())
answer = []

for _ in range(t):
  n = int(input())
  dp = [0] * (n+1)

  for _ in range(n):
    a, b = map(int, input().split())
    dp[a] = b

  min_n = dp[1]
  cnt = 1
  for i in range(2, n + 1):
    if dp[i] < min_n:
      min_n = dp[i]
      cnt += 1
  
  answer.append(cnt)

for ans in answer:
  print(ans)
