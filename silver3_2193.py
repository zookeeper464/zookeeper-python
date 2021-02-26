N=int(input())
bin_list=[0,1,1]
for i in range(2,N+1):
  a=bin_list[i]+bin_list[i-1]
  bin_list.append(a)

temp=bin_list[N]
print(temp)
