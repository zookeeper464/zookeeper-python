N=int(input())
input_list=[0]
for i in range(N):
  a=int(input())
  input_list.append(a)

N_list=[[],[[0,1]],[[0,1,1]]]
if N>2:
  for i in range(3,N+1):
    temp_list=[]
    a,b=N_list[i-2],N_list[i-3]
    for j in a:
      temp=j+[0,1]
      temp_list.append(temp)
    for j in b:
      temp=j+[0,1,1]
      temp_list.append(temp)
    N_list.append(temp_list)

result_list=[]
for i in N_list[N]:
  result=0
  for j in range(N+1):
    result+=i[j]*input_list[j]
  result_list.append(result)

print(max(result_list))
