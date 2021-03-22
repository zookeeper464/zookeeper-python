n = int(input())
dp = [1000]*(1001)
dp[1] = 1
#기본 입력값 설정

for i in range(2,1001):
  dp[i] = i
  for j in range(1,i):
    if i%j !=0:
      pass
    else:
      if dp[i] > dp[j] + i//j:
        dp[i] = dp[j] + i//j
#합성수 일 경우 계산
  if dp[i-1] > dp[i]+1:
    temp = i
    while dp[temp-1] > dp[temp] + 1:
      dp[temp-1] = dp[temp] + 1
      temp -= 1
#갑자기 너무 작은 수가 나올 경우 계산

print(dp[n])
