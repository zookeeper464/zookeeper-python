from math import gcd

t = int(input())
lst = list(map(int,input().split()))
answer = []
for i in range(1,len(lst)):
  g = gcd(lst[0],lst[i])
  answer.append(str(lst[0]//g)+"/"+str(lst[i]//g))

for i in answer:
  print(i)
