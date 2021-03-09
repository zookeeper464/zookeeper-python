N=int(input())
sol=[]
for i in range(N):
  ls=input().split()
  lst=[]
  answer=[]
  for i in ls:
    lst.append(i.split(":"))
  for idx, tm in enumerate(lst):
    a=30*(int(tm[0])%12)+0.5*int(tm[1])
    b=6*int(tm[1])
    x=min(360-abs(b-a),abs(b-a))
    answer.append([idx,tm,x])
  answer=sorted(answer,key=lambda x:[x[2],x[1]])
  y=ls[answer[2][0]]
  sol.append(y)

for i in sol:
  print(i)
