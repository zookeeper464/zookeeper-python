t = int(input())
lst,temp = [], 0
for i in range(1,1000):
  temp += i
  if temp > 1000:
    break
  lst.append(temp)
l = len(lst)
answer = []

for _ in range(t):
  n = int(input())
  for i in range(l):
    if lst[i]>=n:
      break
  
  s = 0
  for a in range(i):
    for b in range(i):
      for c in range(i):
        if lst[a]+lst[b]+lst[c] == n:
          s = 1
          break
      if s == 1:
        break
    if s == 1:
      break
  
  answer.append(s)

print(*answer, sep='\n')
