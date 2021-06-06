import sys
input = sys.stdin.readlines

lst = input()
n = len(lst)
answer = [[] for _ in range(n)]
for i in range(n):
  lst[i] = lst[i].rstrip("\n")
  answer[i].append(sum(x.islower() for x in lst[i]))
  answer[i].append(sum(x.isupper() for x in lst[i]))
  answer[i].append(sum(48<=ord(x)<=57 for x in lst[i]))
  answer[i].append(sum(ord(x)==32 for x in lst[i]))

for i in answer:
  for j in i:
    print(j, end= " ")
  print()
