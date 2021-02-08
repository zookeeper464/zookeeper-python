N=int(input())
val_list=[]
count=0
a=(input().split())[:N]


for v in a:
  v=int(v)
  val_list.append(v)

for i in val_list:
  temp=0
  for j in range(1,i+1):
    if i%j==0:
      temp+=1
  if temp==2:
    count+=1
print(count)
