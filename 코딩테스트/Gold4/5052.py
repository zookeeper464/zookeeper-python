t = int(input())
answer = []

def check(lst):
  l = len(lst)
  for i in range(l-1):
    if len(lst[i])<len(lst[i+1]) and lst[i][0] == lst[i+1][0]:
      if lst[i] == lst[i+1][:len(lst[i])]:
        return 'NO'
  
  return 'YES'

for _ in range(t):
  n = int(input())
  lst = sorted([input() for _ in range(n)])
  answer.append(check(lst))

print('\n'.join(answer))
