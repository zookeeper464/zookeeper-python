N=int(input())
val_list=[]
for i in range(N):
  a=int(input())
  val_list.append(a)


num_list1=[1,0,1]
num_list2=[0,1,1]
for i in range(40):
  num1=num_list1[-1]+num_list1[-2]
  num2=num_list2[-1]+num_list2[-2]
  num_list1.append(num1)
  num_list2.append(num2)

for i in range(N):
  print(num_list1[val_list[i]], num_list2[val_list[i]])
