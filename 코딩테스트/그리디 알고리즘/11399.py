input()
lst = list(map(int,input().split()))
lst.sort()
temp = 0
dp = []
for i in lst:
  temp += i
  dp.append(temp)

print(sum(dp))
