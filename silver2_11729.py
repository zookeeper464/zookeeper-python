N=int(input())
print(2**N-1)
lst=[]
def move(num,start,last,mid,lst):
  if num==1:
    lst.append([start,last])
  else:
    move(num-1,start,mid,last,lst)
    lst.append([start,last])
    move(num-1,mid,last,start,lst)

move(N,1,3,2,lst)

for i in lst:
  for j in range(2):
    print(i[j],end=" ")
  print()
