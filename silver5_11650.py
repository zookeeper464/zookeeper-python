N=int(input())
num_list=[]
for i in range(N):
  a,b=map(int,input().split())
  num_list.append([a,b])

num_list.sort()

for i in num_list:
  print(i[0], i[1])
