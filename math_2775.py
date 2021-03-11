t=int(input())
answer=[]

for i in range(t):
  k=int(input())
  n=int(input())
  lst=list(range(1,n+1))
  for j in range(k):
    for l in range(1,n):
      lst[l]=lst[l]+lst[l-1]
  answer.append(lst[-1])

for i in answer:
  print(i)
