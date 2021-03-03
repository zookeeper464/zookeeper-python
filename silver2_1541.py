st=input().split("-")
answer=0

pl=st[0].split("+")
mi=[]
if len(st)>=1:
  for i in st[1:]:
    mi=mi+i.split("+")
    
for i in pl:
  a=int(i)
  answer+=a

for i in mi:
  a=int(i)
  answer-=a

print(answer)
