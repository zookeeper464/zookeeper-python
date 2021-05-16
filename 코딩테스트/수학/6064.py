from math import gcd

t = int(input())
answer = []
for i in range(t):
  m, n, x, y = map(int,input().split())
  g = gcd(m,n)
  
  #중국인의 나머지 정리
  if (x-y)%g ==0:
    while x < m*n//g:
      if (x-y)%n==0:
        answer.append(x)
        break
      x+= m
  else:
    answer.append(-1)

for i in answer:
  print(i)
