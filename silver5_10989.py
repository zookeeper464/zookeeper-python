N=int(input())
val_list=[]

for i in range(N):
  a=int(input())
  val_list.append(a)
val_list.sort()
for i in range(N):
  print(val_list[i])
