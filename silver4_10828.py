N=int(input())
used_list=[]
val_list=[]

for i in range(N):
  a=input()
  used_list.append(a)

for i in used_list:
  if "push" in i:
    val_list.append(i[-1])
  elif "top" in i:
    if val_list:
      print(val_list[-1])
    else:
      print(-1)
  elif "size" in i:
    print(len(val_list))
  elif "empty" in i:
    if val_list:
      print(0)
    else:
      print(1)
  elif "pop" in i:
    if val_list:
      print(val_list.pop())
    else:
      print(-1)
  else:
    print("ERROR")
