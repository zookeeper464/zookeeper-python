N=int(input())
day_list=[]
val_list=[]
for i in range(N):
  a,b=map(int,input().split())
  day_list.append(a)
  val_list.append(b)

def list_maker(N):
  result_list=[]
  for i in range(2**N):
    temp_list=[0]*int(N)
    a=list(map(int,list(bin(i)[2:])))
    for j in range(1,N+1):
      try:
        temp_list[-j]=a[-j]
      except:
        pass
    result_list.append(temp_list)
  return result_list

def checker(lists,day_list):
  result_list=[]
  for i in lists:
    temp_list=[0]*N
    for j in range(N):
      if i[j]==1:
        for k in range(j,j+day_list[j]):
          try:
            temp_list[k]+=1
          except:
            for v in range(N):
              temp_list[v]+=100
    if max(temp_list)<=1:
      result_list.append(i)
  return result_list

def max_maker(lists,val_list):
  temp_list=[]
  for i in lists:
    temp_num=0
    for j in range(N):
      if i[j]:
        temp_num+=val_list[j]
    temp_list.append(temp_num)
  max_num=max(temp_list)
  print(max_num)

max_maker(checker(list_maker(N),day_list),val_list)
