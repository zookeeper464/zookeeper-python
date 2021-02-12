N=int(input())
M=int(input())
vir_list=[]
for i in range(M):
  a,b=map(int,input().split())
  [a,b].sort()
  vir_list.append([a,b])
vir_list.sort()
count=set([1])

for i in vir_list:
  i=set(i)
  if i&count!=set():
    count=i|count

length=len(count)-1
print(length)
