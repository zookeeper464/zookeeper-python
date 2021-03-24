k = int(input())
lst = []
for i in range(k):
  temp = int(input())
  if temp != 0:
    lst.append(temp)
  else:
    lst.pop()

print(sum(lst))
