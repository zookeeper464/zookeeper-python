lst = list(input())
s = False
m = 0
for i in lst:
  if i == '0':
    s = True
  else:
    m += int(i)

if s and m%3==0:
  lst.sort(reverse=True)
  print(''.join(lst))
else:
  print(-1)
