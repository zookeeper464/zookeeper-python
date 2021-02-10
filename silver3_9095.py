N=int(input())
input_list=[]
for i in range(N):
  a=int(input())
  input_list.append(a)

M=max(input_list)
result_list=[0]*(M+1)
result_list[1]=1
try:
  result_list[2]=2
except:
  pass
try:
  result_list[3]=4
except:
  pass

for i in range(4,M+1):
  result_list[i]=result_list[i-1]+result_list[i-2]+result_list[i-3]

for i in input_list:
  print(result_list[i])
