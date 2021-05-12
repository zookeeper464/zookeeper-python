t = int(input())
answer = []
lst = [1,1,1,2,2]
for i in range(t):
  n = int(input())
  while len(lst)<n:
    lst.append(lst[-1]+lst[-5])
  answer.append(lst[n-1])

for i in answer:
  print(i)
