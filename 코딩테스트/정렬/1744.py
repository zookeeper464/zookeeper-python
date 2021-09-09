n = int(input())
mlst,plst,answer = [],[],0
for _ in range(n):
  s = int(input())
  if s>1:
    plst.append(s)
  elif s==1:
    answer += 1
  else:
    mlst.append(s)

plst.sort(reverse=True)
mlst.sort()
for i in range(len(plst)//2):
  answer += plst[2*i]*plst[2*i+1]

for i in range(len(mlst)//2):
  answer += mlst[2*i]*mlst[2*i+1]

if len(plst)%2==1:
  answer += plst[-1]

if len(mlst)%2==1:
  answer += mlst[-1]

print(answer)
