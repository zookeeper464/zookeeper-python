answer = []
while True:
  s = input()[::-1]
  if s == 'DNE':
    break
  answer.append(s)

for ans in answer:
  print(ans)
