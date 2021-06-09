n, m = map(int,input().split())
answer = ""
while n>0:
  temp = n%m
  if temp>9:
    s = chr(55+temp)
  else:
    s = str(temp)
  answer = s+answer
  n //= m
print(answer)
