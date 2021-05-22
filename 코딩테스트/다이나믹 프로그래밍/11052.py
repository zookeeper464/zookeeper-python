n = int(input())
lst = [0]+list(map(int,input().split()))
for i in range(2,n+1):
  for j in range(i//2+1):
    lst[i] = max(lst[j]+lst[i-j],lst[i])
print(lst[-1])
