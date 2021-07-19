answer = []
def check (lst, n):
  dp = [0]*n
  temp = set()
  for i in range(n):
    temp_list = list(temp)
    for j in temp_list:
      if lst[i]<lst[j]:
        dp[j] = lst[j]*(i-j)
        temp -= {j}
    temp.add(i)
  for i in range(n):
    if dp[i] == 0:
      dp[i] = lst[i]*(n-i)
  return max(dp)

while True:
  lst = list(map(int,input().split()))
  n = lst[0]
  lst = lst[1:]
  if n == 0:
    break
  answer.append(check(lst, n))

for ans in answer:
  print(ans)
