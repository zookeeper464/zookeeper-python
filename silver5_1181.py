N=int(input())
str_list=[]
for i in range(50):
  str_list.append([])

for i in range(N):
  a=input()
  n=len(a)
  if a not in str_list[n-1]:
    str_list[n-1].append(a)

for i in range(50):
  if str_list[i]:
    str_list[i].sort()

for i in range(50):
  if str_list[i]:
    for j in str_list[i]:
      print(j)
