lst = [int(input()) for _ in range(9)]
temp = sum(lst)-100
answer = []
for i in range(8):
  for j in range(i+1,9):
    if lst[i]+lst[j] == temp:
      for k in range(9):
        if k not in (i,j):
          answer.append(lst[k])
      break
  if answer:
    break

print(*sorted(answer),sep='\n')
