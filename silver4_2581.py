M=int(input())
N=int(input())

num1=0
num2=0
for i in range(M,N+1):
  count=0
  for j in range(2,min(100,i)):
    if i%j==0:
      count+=1
  if count==0 and i!=1:
    if num1==0:
      num2=i
    num1+=i
if num1==0:
  print(-1)
else:
  print(num1)
  print(num2)
