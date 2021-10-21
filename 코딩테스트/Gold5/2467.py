def check ():
  if minus == []:
    return plus[0],plus[1]
  
  if plus ==[]:
    return minus[1],minus[0]

  a,b,m,p,temp = minus[0],plus[0],0,0,abs(plus[0]+minus[0])
  while True:
    if plus[p]+minus[m]>0:
      if temp>abs(plus[p]+minus[m]):
        temp = abs(plus[p]+minus[m])
        a,b = minus[m],plus[p]
      
      m += 1
      if m == len(minus):
        break

    elif plus[p]+minus[m] == 0:
      return minus[m],plus[p]
      
    else:
      if temp>abs(plus[p]+minus[m]):
        temp = abs(plus[p]+minus[m])
        a,b = minus[m],plus[p]

      p += 1
      if p == len(plus):
        break

  if len(minus)>1:
    if temp > -(minus[0]+minus[1]):
      a,b = minus[1],minus[0]
  
  if len(plus)>1:
    if abs(a+b) > plus[0]+plus[1]:
      a,b = plus[0],plus[1]
  
  return a,b    

n = int(input())
plus,minus = [],[]
for i in map(int,input().split()):
  if i >0:
    plus.append(i)
  else:
    minus.append(i)

plus.sort()
minus.sort(reverse=True)

print(*check())
