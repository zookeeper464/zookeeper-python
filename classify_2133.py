n=int(input())
lst=[1,3]
m=1
if n%2==1:
  print(0)
elif 1<=n<=30:
  for i in range(n//2-1):
    lst.append(3*lst[-1]+m*2)
    m+=lst[-2]  
  print(lst[-1])
