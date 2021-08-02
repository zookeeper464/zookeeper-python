n,m = int(input()), int(input())
lst = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int,input().split())
  lst[a].append(b)
  lst[b].append(a)

temp = lst[1][:]
answer = set(lst[1]+[1])
while temp:
  t = temp.pop()
  for i in lst[t]:
    if i not in answer:
      temp.append(i)
      answer = answer|set([i])

print(len(answer)-1)
