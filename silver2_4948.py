import math

lst=[]
while True:
  N=int(input())
  if N==0:
    break
  lst.append(N)

M=max(lst)
p_lst=[]
for i in range(2,2*M+1):
  count=0
  for j in range(2,int(math.sqrt(i))+1):
    if i%j==0:
      count+=1
      break
  if count==0:
    p_lst.append(i)

for i in lst:
  count=0
  for j in p_lst:
    if j>i and j<=2*i:
      count+=1
    elif j>2*i:
      break
  print(count)
