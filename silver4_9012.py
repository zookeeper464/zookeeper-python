N=int(input())
val_list=[]

for i in range(N):
  a=input()
  val_list.append(a)

for i in val_list:
  temp1=i.count(')')
  temp2=i.count('(')
  if temp1==temp2:
    print("YES")
  else:
    print("NO")
