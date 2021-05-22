n = int(input())
lst = [1 for _ in range(10)]
lst[0]=0
temp = lst[:]
for i in range(1,n):
  lst[0],lst[-1] = temp[1],temp[-2]
  for j in range(1,9):
    lst[j] = temp[j-1]+temp[j+1]
  temp = lst[:]
print(sum(lst))
