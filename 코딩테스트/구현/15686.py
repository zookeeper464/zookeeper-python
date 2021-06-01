from itertools import combinations as cb

n,m = map(int,input().split())
lst1 = []
lst2 = []
for i in range(n):
  ls = list(map(int,input().split()))
  for j in range(n):
    if ls[j] == 1:
      lst1.append([i,j])
    if ls[j] == 2:
      lst2.append([i,j])

dp = [[] for _ in range(len(lst1))]
for i in range(len(lst1)):
  for j in range(len(lst2)):
    dp[i].append(abs(lst1[i][0]-lst2[j][0])+abs(lst1[i][1]-lst2[j][1]))

results = list(cb(range(len(lst2)), m))

answers = []
for result in results:
  answer = 0
  for i in dp:
    temp = 2*n
    for j in result:
      temp = min(i[j], temp)
    answer += temp
  answers.append(answer)

print(min(answers))
