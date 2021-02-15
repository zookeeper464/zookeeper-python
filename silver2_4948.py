def checker (n):
  global count
  for i in range(n+1,2*n+1):
    temp=0
    for j in range(1,i):
      if i%j==0:
        temp+=1
    if temp==1:
      count+=1

val_list=[]
T=1
while T>0 and T<=123456:
  T=int(input())
  val_list.append(T)
  if T==0:
    break

count=0
for i in val_list:
  checker(i)

print(count)
