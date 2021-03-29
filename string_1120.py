a, b = input().split()

na = len(a)
nb = len(b)

answer = nb
for i in range(nb-na+1):
  temp = 0
  for j in range(na):
    if a[j] != b[i+j]:
      temp += 1
  if temp < answer:
    answer = temp

print(answer)
