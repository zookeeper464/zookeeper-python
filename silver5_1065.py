N=int(input())
count=0

for i in range(1,N+1):
  a=i//100
  b=(i//10)%10
  c=i%10
  if a==0:
    count+=1
  elif a-b==b-c:
    count+=1

if N<=1000 and N>0:
  print(count)
else:
  print("ERROR")
