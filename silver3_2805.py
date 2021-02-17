N,M=map(int,input().split())
N_list=list(map(int,input().split()))[:N]

K=max(N_list)
tree=0
num=0
while M!=tree:
  num+=1
  K-=1
  for i in N_list:
    if i>K:
      tree+=1
  
print(K)
