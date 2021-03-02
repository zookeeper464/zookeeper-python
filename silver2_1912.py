N=int(input())
lst=list(map(int,input().split()))
sol=[]
for i in range(N):
  sol.append(0)

def checker(sol,lst,i,N):
  if i==0:
    sol[i]=lst[i]
  else:
    if sol[i-1]>0:
      sol[i]=sol[i-1]+lst[i]
    else:
      sol[i]=lst[i]
for i in range(N):
  checker(sol,lst,i,N)
  
print(max(sol))
