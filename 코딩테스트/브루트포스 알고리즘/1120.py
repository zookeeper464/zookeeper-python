a,b = input().split()
la,lb = len(a), len(b)
answer = lb

for i in range(lb-la+1):
  temp = 0
  for j in range(la):
    if a[j] != b[i+j]:
      temp += 1
  if answer > temp:
    answer = temp
    
print(answer)
