N=int(input())
result_list=[0]*(N+1)
try:
  result_list[2]=1
except:
  pass
try:
  result_list[3]=1
except:
  pass

for i in range(4,N+1):
  if i%6==0:
    result_list[i]=1+min(result_list[i//3],result_list[i//2],result_list[i-1])
  elif i%3==0:
    result_list[i]=1+min(result_list[i//3],result_list[i-1])
  elif i%2==0:
    result_list[i]=1+min(result_list[i//2],result_list[i-1])
  else:
    result_list[i]=1+result_list[i-1]

print(result_list[N])
