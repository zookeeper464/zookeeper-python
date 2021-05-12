lst = []
while True:
  a,b,c = map(int,input().split())
  if (a,b,c) == (0,0,0):
    break
  temp = [a,b,c]
  temp.sort()
  if temp[-1]**2 == temp[0]**2+temp[1]**2:
    lst.append("right")
  else:
    lst.append("wrong")

for i in lst:
  print(i)
