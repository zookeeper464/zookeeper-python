n=int(input())
llst=[]
for i in range(n):
  lst=list(map(int,input().split()))
  m=len(llst)
  if m==0:
    temp=[lst[0]]
  else:
    temp=[llst[0]+lst[0]]
    for j in range(1,m):
      temp.append(max(llst[j],llst[j-1])+lst[j])
    temp.append(llst[-1]+lst[-1])
  llst=temp[:]

print(max(llst))
