n = int(input())
q= []
answer = []

def command (s):
  if len(s.split()) == 1:
    if s[0] == "e":
      if q:
        return 0
      else:
        return 1
    
    elif s[0] == "s":
      return len(q)
    
    if q:
      num = q.pop()
    else:
      return -1

    if s[0] == "t":
      q.append(num)
    return num
  
  else:
    num = s.split()[1]
    q.append(num)
    return "False"

for _ in range(n):
  s = input()
  temp = command(s)
  if temp != "False":
    answer.append(temp)

for ans in answer:
  print(ans)
