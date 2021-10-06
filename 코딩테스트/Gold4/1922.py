from heapq import heappop, heappush

n,m = int(input()),int(input())
dp = [[] for _ in range(n+1)]
for _ in range(m):
  a,b,c = map(int,input().split())
  dp[a].append([c,b])
  dp[b].append([c,a])

st,num,answer,hq = {1}, 1, 0, []

while num:
  if len(st) == n:
    break

  for val, idx in dp[num]:
    if idx not in st:
      heappush(hq,[val,idx])

  for _ in range(len(hq)):
    val, idx = heappop(hq)
    if idx not in st:
      answer += val
      num = idx
      st.add(num)
      break
  
print(answer)
