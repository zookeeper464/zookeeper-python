n = int(input())
distinct = list(map(int,input().split()))
cost = list(map(int,input().split()))

temp = cost[0]
for i in range(1,n):
  if cost[i] > temp:
    cost[i] = temp
  else:
    temp = cost[i]

answer = 0
for i in range(n-1):
  answer += distinct[i]*cost[i]

print(answer)
