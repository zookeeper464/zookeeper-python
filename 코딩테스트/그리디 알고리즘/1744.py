n = int(input())
mlst = []
plst = []
answer = 0
for _ in range(n):
  m =int(input())
  if m > 1:
    plst.append(m)
  elif m ==1:
    answer += 1
  else:
    mlst.append(m)

plst.sort(reverse = True)
mlst.sort()

for i in range(1,len(plst),2):
  answer += plst[i]*plst[i-1]
for i in range(1,len(mlst),2):
  answer += mlst[i]*mlst[i-1]

if len(plst)%2==1:
  answer += plst[-1]
if len(mlst)%2==1:
  answer += mlst[-1]

print(answer)
