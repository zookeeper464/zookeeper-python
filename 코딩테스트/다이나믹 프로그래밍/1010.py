from math import comb

t = int(input())
answer = []
for i in range(t):
  a,b = map(int,input().split())
  answer.append(comb(b,a))

for i in answer:
  print(i)
