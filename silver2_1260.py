N,M,V=map(int,input().split())
M_list=[]
temp_list=V_list=[V]
for i in range(M):
  a,b=map(int,input().split())
  M_list.append([a,b])
  M_list.append([b,a])
M_list.sort()

