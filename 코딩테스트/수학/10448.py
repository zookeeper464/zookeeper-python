t = int(input())

dp = [0 for _ in range(1001)]
temp = [x*(x+1)//2 for x in range(45)]
for i in range(1,45):
  a = temp[i]
  for j in range(1,45):
    b = temp[j]
    for k in range(1,45):
      c = temp[k]
      if a+b+c<=1000:
        dp[a+b+c] = 1
      else:
        break

answer = []
for _ in range(t):
  answer.append(dp[int(input())])

for i in answer:
  print(i)
