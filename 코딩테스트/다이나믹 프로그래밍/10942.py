n = int(input())
lst = list(map(int, input().split()))
m = int(input())
answer=[]
dp=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
  dp[i][i] = 1

for i in range(n):
  for start in range(n-i):
    end = start + i
    if lst[start] == lst[end]:
      if i == 1:
        dp[start][end] = 1
      elif dp[start+1][end-1] != 0:
        dp[start][end] = 1

for i in range(m):
  s, e = map(int, input().split())
  answer.append(dp[s-1][e-1])

for i in answer:
  print(i)
