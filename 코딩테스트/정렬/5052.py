t = int(input())
answer = []

for _ in range(t):
  n = int(input())
  lst = sorted([input() for _ in range(n)])
  s = "YES"
  for i in range(n-1):
    if s =='NO':
      break
    
    if len(lst[i]) > len(lst[i+1]):
      pass
    elif lst[i] == lst[i+1][:len(lst[i])]:
      s = 'NO'

  answer.append(s)

print(*answer, sep='\n')
