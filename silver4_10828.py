def form (put):
  global val_list, used_list
  if "push" in put:
    put=put.split()
    val_list.append(str(put[-1]))

  elif put=="pop":
    if val_list==[]:
      used_list.append(-1)
    else:
      used_list.append(val_list.pop())
  
  elif put=="size":
    used_list.append(len(val_list))

  elif put=="empty":
    if val_list==[]:
      used_list.append(1)
    else:
      used_list.append(0)

  elif put=="top":
    if val_list==[]:
      used_list.append(-1)
    else:
      used_list.append(val_list[-1])


N=int(input())
used_list=[]
val_list=[]

for i in range(N):
  a=input()
  form(a)

for i in used_list:
  print(i)
