import sys
input=sys.stdin.readline

lst=[]
a = [False]*2 + [True]*999999
plst=[]
answer=[]

for i in range(2,1000001):
  if a[i]:
    plst.append(i)
    for j in range(2*i, 1000001, i):
        a[j] = False

while True:
  n=int(input())
  if n==0:
    break
  lst.append(n)

for i in lst:
  x=True
  for j in plst:
    if a[i-j]:
      answer.append(f"{i} = {j} + {i-j}")
      x=False
      break
  if x:
    answer.append("Goldbach's conjecture is wrong.")

for i in answer:
  print(i)
