N=int(input())
lst=list(map(int,input().split()))
sol=[]
for i in range(N):
  sol.append(0)

def checker(sol,lst,i,N):
  if i==N-1:
    sol[i]=1
  else:
    temp=[0]
    for j in range(i+1,N):
      if lst[j]>lst[i]:
        temp.append(sol[j])
    sol[i]=max(temp)+1

for i in range(N-1,-1,-1):
  checker(sol,lst,i,N)

print(max(sol))
