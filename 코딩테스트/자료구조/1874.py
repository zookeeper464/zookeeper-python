n = int(input())
s, answer = [], []
count = 1
temp = True

for i in range(n):
  num = int(input())

  while count <= num:
    s.append(count)
    answer.append('+')
    count += 1

  if s[-1] == num:
    s.pop()
    answer.append('-')
  else:
    temp = False

if temp:
  for ans in answer:
    print(ans)
else:  
  print('NO')
