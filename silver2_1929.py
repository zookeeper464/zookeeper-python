N,M=map(int,input().split())
p_list=list(range(N,M+1))
temp_list=[]


for i in p_list:
  count=0
  for j in range(1,i):
    if i%j==0:
      count+=1
  if count==1:
    print(i)
