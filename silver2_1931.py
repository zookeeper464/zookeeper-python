count=0
n=int(input())
val_list=[]
for i in range(n):
  a,b=map(int,input().split())
  val_list.append([a,b])
val_list.sort()
temp_list=val_list
for i in temp_list:
  for j in temp_list:
    if i[0]<=j[0] and i[1]>j[1] and i in val_list:
      val_list.remove(i)

while 1:
  temp_list=[]
  for i in val_list:
    temp_list.append(i[1])
  a=min(temp_list)
  count+=1
  temp_list=val_list[:]
  for i in temp_list:
    if i[0]<a:
      val_list.remove(i)
  if val_list==[]:
    break

print(count)
