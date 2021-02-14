T=int(input())
val_list=[]

def checker(n):
  if n==1:
    return [[1],[2]]
  elif n==2:
    return [[1,2],[2,1]]
  else:
    temp1=checker(n-1)
    for i in temp1:
      if i[-1]==1:
        i.append(2)
      elif i[-1]==2:
        i.append(1)
    temp2=checker(n-2)
    for i in temp2:
      if i[-1]==1:
        i.append(0)
        i.append(2)
      elif i[-1]==2:
        i.append(0)
        i.append(1)
    return temp1+temp2

def return_checker(lists,list1,list2):
  global temp_list
  for i in lists:
    temp=0
    num=0
    for j in i:
      if j==1:
        temp+=list1[num]
      elif j==2:
        temp+=list2[num]
      num+=1
    temp_list.append(temp)
  return max(temp_list)


for i in range(T):
  temp_list=[]
  n=int(input())
  temp_list1=list(map(int, input().split()))[:n]
  temp_list2=list(map(int, input().split()))[:n]
  lists=checker(n)
  a=return_checker(lists,temp_list1,temp_list2)
  val_list.append(a)

for i in range(T):
  print(val_list[i])
