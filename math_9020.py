n=int(input())
lst=[]
a = [False]*2 + [True]*9999
plst=[]

for i in range(2,10001):
  if a[i]:
    plst.append(i)
    for j in range(2*i, 10001, i):
        a[j] = False

for i in range(n):
  e=int(input())
  for j in range(e//2-1):
    if e//2-j in plst and e//2+j in plst:
      lst.append(f"{e//2-j} {e//2+j}")
      break

for i in lst:
  print(i)
