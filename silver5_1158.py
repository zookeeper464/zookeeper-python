N,K=map(int,input().split())
val_list=list(range(1,N+1))
result_list=[]

print("<", end="")
temp=-1
result=0
for i in list(range(1,N)):
  temp+=K
  temp=temp%N
  result=val_list[temp]
  print(result, end=", ")
print(f"{val_list[-1]}>")
