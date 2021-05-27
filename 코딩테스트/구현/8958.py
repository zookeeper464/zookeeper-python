n = int(input())
answer = []
for _ in range(n):
  lst = list(input())
  m = len(lst)
  dp = [0 for _ in range(m)]
  if lst[0] == "O": dp[0]=1
  for i in range(1,m):
    if lst[i] == "X":
      dp[i] = 0
    else:
      dp[i] = dp[i-1]+1
  answer.append(sum(dp))

for i in answer:
  print(i)
