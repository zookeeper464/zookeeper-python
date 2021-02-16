result_list=[]
count=0
N,S=map(int, input().split())

val_list=list(map(int,input().split()))[:N]

for i in range(N):
  for j in range(i):
    if sum(val_list[j:i])==S:
      count+=1

print(count)
    
