n = int(input())
answer = []

for i in range(n):
  s = input()
  dp = [0] * len(s)
  if s[0] =="O":
    dp[0] =1
  for j in range(1,len(s)):
    if s[j] == "O":
      dp[j] = dp[j-1] +1
  answer.append(sum(dp))
  
for i in answer:
  print(i)
