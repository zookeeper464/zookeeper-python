n=int(input())
lst=[]
for i in range(n):
  h,w,num=map(int,input().split())
  a=(num-1)%h+1
  b=(num-1)//h+1
  answer=100*a+b
  lst.append(answer)

for i in lst:
  print(int(i))

