n = int(input())
dp = [0, 1, 2]
if n>2:
  for i in range(3,n+1):
    dp.append((dp[-1]+dp[-2])%10007)
print(dp[-1])
