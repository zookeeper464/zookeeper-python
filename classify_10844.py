n=int(input())
lst=[1,1,1,1,1,1,1,1,1,1]
for i in range(n-1):
  temp=[]
  temp.append(lst[1])
  for i in range(1,9):
    temp.append(lst[i-1]+lst[i+1])
  temp.append(lst[-2])
  lst=temp[:]

print(sum(lst[1:])%(10**9))
