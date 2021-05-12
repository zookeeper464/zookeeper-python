t = int(input())
answer = []

for i in range(t):
  lst = list(map(int,input().split()))
  r1, r2 = lst[2], lst[-1]
  dx, dy = abs(lst[0]-lst[3]), abs(lst[1]-lst[4])
  dd = dx**2+dy**2
  if (dx,dy,r1-r2)==(0,0,0):
    answer.append(-1)
  elif dd==(r1+r2)**2 or dd==(r1-r2)**2:
    answer.append(1)
  elif dd>(r1+r2)**2 or dd<(r1-r2)**2:
    answer.append(0)
  else:
    answer.append(2)

for i in answer:
  print(i)
