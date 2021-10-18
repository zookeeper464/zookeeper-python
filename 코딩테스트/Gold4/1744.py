n = int(input())
minus,answer,plus = [],0,[]
for _ in range(n):
  m = int(input())
  if m == 1:
    answer += 1
  elif m <1:
    minus.append(m)
  else:
    plus.append(m)

minus.sort()
plus.sort(reverse=True)

for i in range(0,len(minus),2):
  try:
    answer += minus[i]*minus[i+1]
  except:
    answer += minus[i]

for i in range(0,len(plus),2):
  try:
    answer += plus[i]*plus[i+1]
  except:
    answer += plus[i]

print(answer)
