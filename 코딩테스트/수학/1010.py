from math import comb

n = int(input())
answer = []

for i in range(n):
  a, b = map(int,input().split())
  answer.append(comb(b,a))

for i in answer:
  print(i)
