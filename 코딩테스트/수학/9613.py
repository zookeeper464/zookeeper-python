from math import gcd

t = int(input())
answer = []
for _ in range(t):
  lst = list(map(int,input().split()))
  temp = 0
  for i in range(1,lst[0]+1):
    for j in range(i+1,lst[0]+1):
      temp += gcd(lst[i],lst[j])
  answer.append(temp)

for i in answer:
  print(i)
