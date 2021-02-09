N=int(input())
location_list=[]

temp=input().split()[:N]
N_list=list(map(int,temp))

M=int(input())
temp=input().split()[:M]
M_list=map(int,temp)

for i in M_list:
  if i in N_list:
    print(1)
  else:
    print(0)
