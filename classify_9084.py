t = int(input())
answer = []
for i in range(t):
  n = int(input())
  lst = list(map(int,input().split()))
  m = int(input())
  dp = [0] * (m+1)
  #입력하는 부분

  for j in lst:
    if j < m+1:
      dp[j] += 1
      for k in range(m+1):
        if dp[k] !=0 and k+j < m+1:
          dp[k+j] += dp[k]
  answer.append(dp[-1])
  #각 상황에 맞는 dp 계산

for i in answer:
  print(i)
