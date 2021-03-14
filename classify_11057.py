n=int(input())
lst=[1]*10
for i in range(n-1):
  for i,v in enumerate(lst):
    lst[i]=sum(lst[i:])
print(sum(lst)%10007)
