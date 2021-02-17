N=int(input())
N_list=[]
while N<=100 and N>0:
  if N<=20:
    a=list(map(int,input().split()))[:N]
    for i in a:
      N_list.append(i)
    break
  else:
    a=list(map(int,input().split()))[:20]
    for i in a:
      N_list.append(i)
    N-=20


M=int(input())
for i in range(M):
  a, b=map(int,input().split())
  if a==1:
    for i in range(N//b):
      N_list[3*i+2]+=1
      N_list[3*i+2]%=2
      print(i)
  elif a==2:
    b-=1
    j=0
    try:
      while N_list[b-j]==N_list[b+j]:
        j+=1
    except:
      pass
    for k in range(b-j+1,b+j):
      N_list[k]+=1
      N_list[k]%=2

print(N_list)
