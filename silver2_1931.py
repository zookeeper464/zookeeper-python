N=int(input())
lst=[]
for i in range(N):
  a,b=map(int,input().split())
  lst.append([a,b])
count=0

lst.sort(key=lambda x : [x[1], x[0]])

temp=0
for i in lst:
  if i[0]>=temp:
    count+=1
    temp=i[1]


print(count)
