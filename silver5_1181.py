N=int(input())
str_list=[]
for i in range(N):
  a=input()
  str_list.append(a)

str_list.sort()
str_list.sort(key=lambda x:len(x))

for i in str_list:
  print(i)
