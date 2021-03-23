n, m = int(input()), int(input())

answer = 1
temp = 0
a=0
lst = []
if m:
  for i in range(m):
    a = int(input())
    lst.append(a-temp-1)
    temp = a
lst.append(n-a)
k = max(lst)
# 입력값 변환

dp = [1] * (k+1)
for i in range(2,k+1):
  dp[i] = dp[i-1] + dp[i-2]
# dp 생성

for i in lst:
  answer *= dp[i]

print(answer)
