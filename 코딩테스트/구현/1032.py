n = int(input())
st = list(map(set,list(input())))
for _ in range(n-1):
  temp = list(input())
  for i in range(len(st)):
    st[i].add(temp[i])

for i in range(len(st)):
  if len(st[i])==1:
    print(temp[i],end="")
  else:
    print("?",end="")
