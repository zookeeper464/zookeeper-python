n=int(input())
lst=[0,0,0]
temp=[0,0,0]
for i in range(n):
  r,b,g=map(int,input().split())
  lst[0]=min(temp[1:3])+r
  lst[1]=min(temp[0::2])+b
  lst[2]=min(temp[:2])+g
  temp=lst[:]
  
print(min(lst))
