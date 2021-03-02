T=int(input())
answer=[]
for i in range(T):
  N=int(input())
  lst=[]
  lst1=list(map(int,input().split()))
  lst2=list(map(int,input().split()))

  for j in range(N):
    if j==0:
      lst.append([lst1[0],lst2[0]])
    elif j==1:
      lst.append([lst1[1]+lst2[0],lst2[1]+lst1[0]])
    else:
      lst.append([lst1[j]+max(lst[j-1][1],lst[j-2][1]),lst2[j]+max(lst[j-1][0],lst[j-2][0])])

  answer.append(max(lst[-1]))
  
for i in answer:
  print(i)
