visited=[False]+[True]*10100
num=1
while True:
  s=str(num)
  temp=num
  for i in s:
    temp+=int(i)
  if num>10000:
    break
  visited[temp]=False
  num+=1
  
for i in range(10001):
  if visited[i]:
    print(i)
