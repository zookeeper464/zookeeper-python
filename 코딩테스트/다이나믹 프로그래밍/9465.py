t = int(input())
answer = []

for _ in range(t):
  n = int(input())
  lst1 = list(map(int,input().split()))
  lst2 = list(map(int,input().split()))
  if n>1:
    lst1[1] += lst2[0]
    lst2[1] += lst1[0]
    for i in range(2,n):
      lst1[i] = lst1[i] + max(lst2[i-1],lst2[i-2])
      lst2[i] = lst2[i] + max(lst1[i-1],lst1[i-2])
  answer.append(max(lst1[-1],lst2[-1]))

for i in answer:
  print(i)
