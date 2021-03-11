n = int(input())
answer=[]

for i in range(n):
  lst=list(map(int,input().split()))
  num=lst[0]
  ev=sum(lst[1:])/num
  sol=0
  for i in lst[1:]:
    if i>ev:
      sol+=1
  answer.append(sol/num*100)

for i in answer:
  print("{:.3f}%".format(i))
