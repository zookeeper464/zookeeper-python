N=int(input())
val_list=[]
for i in range(N):
  a=int(input())
  val_list.append(a)

bin_list=[0,1,1,1,2,2]
for i in range(max(val_list)):
  a=bin_list[i+1]+bin_list[i+5]
  bin_list.append(a)

for i in val_list:
  print(bin_list[i])
