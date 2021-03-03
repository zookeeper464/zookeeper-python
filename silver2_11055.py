N=int(input())
lst=list(map(int,input().split()))
sol=lst[:]

for i in range(1,N):
  for j in range(i):
    if lst[i]>lst[j] and lst[i]+sol[j]>sol[i]:
      sol[i]=lst[i]+sol[j]

print(max(sol))
