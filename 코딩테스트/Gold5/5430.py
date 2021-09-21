t = int(input())
answers = []

for _ in range(t):
  s = input()
  n = int(input())
  lst = input()[1:-1].split(',')
  start,end = 0, n
  cnt = 0
  for i in s:
    if i == 'R':
      cnt = (cnt+1)%2
    else:
      if cnt == 1:
        end -= 1
      else:
        start += 1

    if start>end:
      answer = 'error'
      break

  if start <= end:
    if cnt == 0:
      answer = "["+ ",".join(lst[start:end])+ "]"
    else:
      answer = "["+ ",".join(lst[start:end][::-1])+ "]"
  answers.append(answer)

for ans in answers:
  print(ans)
