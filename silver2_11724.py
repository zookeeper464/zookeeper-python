count=0
N,M=map(int,input().split())
val_list=[]
for i in range(M):
  a,b=map(int,input().split())
  if a>b:
    b,a=a,b
  val_list.append([a,b])
val_list.sort()

temp_list=[]
for i in range(1,N+1):#1~N까지
  if i in temp_list:#temp_list에 없을때만 사용하는 것
    pass
  else:#temp_list에 없으면 실행
    temp_list.append(i)#이제 추가한다.
    temp_set={i}#i에 대한 새로운 집합생성
    for j in val_list:
      set_j=set(j)
      if temp_set&set_j==set():
        pass
      else:
        temp_set=temp_set|set_j
    count+=1
    temp_list=list(set(temp_list)|temp_set)
    print(temp_list)
print(count)
