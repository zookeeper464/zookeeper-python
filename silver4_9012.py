N=int(input())
val_list=[]

for i in range(N):
  a=input()
  val_list.append(a)

for i in val_list:
  count=0
  for j in i:
    if j=="(":
      count+=1
    elif j==")":
      count-=1
    if count<0:
      break
  if count==0:
    print("YES")
  else:
    print("NO")
