N=int(input())
time_list=list(range(1,N+1))
time_list.reverse()

input_list=list(map(int,input().split()))[:N]

results=0
input_list.sort()
for i in range(N):
  results+=time_list[i]*input_list[i]

print(results)
