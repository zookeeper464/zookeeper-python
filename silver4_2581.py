M=int(input())
N=int(input())
factor_list=[]

if M<=N:
  for i in range(M,N+1):
    count=0
    for j in range(1,i+1):
      if i%j==0:
        count+=1
    if count==2:
      factor_list.append(i)
print(sum(factor_list))
print(min(factor_list))
