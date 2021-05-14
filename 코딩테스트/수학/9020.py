plst = [True for i in range(9999)]
plst[0],plst[1] = False, False

for i in range(2,9999):
  if plst[i]:
    j = 2
    while i*j<9999:
      plst[i*j] = False
      j += 1

t = int(input())
answer = []
for i in range(t):
  n = int(input())
  for j in range(n//2,2,-1):
    if plst[j] and plst[n-j]:
      answer.append([str(j),str(n-j)])
      break

for i in answer:
  print(" ".join(i))
