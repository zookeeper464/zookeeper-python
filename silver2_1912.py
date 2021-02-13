n=int(input())
a=list(map(int,input().split()))[:n]
val_list=[]

def sum(N,M):
  global a
  temp=0
  for i in range(N,M+1):
    temp+=a[i]
  val_list.append(temp)

for i in range(n):
  for j in range(i,n):
    sum(i,j)
print(max(val_list))
