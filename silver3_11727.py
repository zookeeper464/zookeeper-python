N=int(input())
bin_list=[1,1]
for i in range(N):
  a=bin_list[i]*2+bin_list[i+1]
  bin_list.append(a)

print(bin_list[N])
