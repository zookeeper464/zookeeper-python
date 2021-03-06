N=int(input())
A=list(map(int,input().split()))
lst=[1]*N

for i in range(N):
  for j in range(i):
    if A[i]>A[j] and lst[i]<=lst[j]:
      lst[i]=lst[j]+1

print(max(lst))
