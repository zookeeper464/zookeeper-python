N=int(input())
input_list=[]

result_list=[0]*(N+1)
result_list[1]=1
try:
  result_list[2]=2
except:
  pass
  

for i in range(3,N+1):
  result_list[i]=result_list[i-1]+result_list[i-2]

print(result_list[N]%10007)
