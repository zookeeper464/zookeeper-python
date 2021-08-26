n = int(input())
lst = list(map(int,input().split()))
dp = [[] for _ in range(n)]
m = int(input())
root, answer = 0,0

for idx, i in enumerate(lst):
  if i == -1:
    root = idx
  elif i == m:
    pass
  elif idx == m:
    pass
  else:
    dp[i].append(idx)

if root == m:
  pass
else:
  temp = [root]
  while temp:
    t = temp.pop()
    if len(dp[t]) == 0:
      answer += 1
    else:
      temp += dp[t]

print(answer)
