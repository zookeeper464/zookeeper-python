v=int(input())
e=int(input())
e_lst=[]
for i in range(e):
  a=list(map(int,input().split()))
  e_lst.append(a)


lst2=[1]

while True:
  lst1=[]
  lst3=[]
  for i in e_lst:
    for j in lst2:
      if j in i:
        lst1=lst1+i
        
  for i in lst1:
    if i not in lst2:
      lst2.append(i)
      lst3.append(i)
  if lst3==[]:
    break

print(len(lst2)-1)
