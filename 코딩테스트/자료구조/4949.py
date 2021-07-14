answer = []

def check (s):
  lst = []
  for i in s:
    if i in "([":
      lst.append(i)
    if i == ")":
      if lst ==[]:
        return "no"
      elif lst[-1] == "(":
        lst.pop()
      else:
        return 'no'
    if i == ']':
      if lst == []:
        return 'no'
      elif lst[-1] == '[':
        lst.pop()
      else:
        return 'no'
  if lst:
    return 'no'
  return "yes"

while True:
  s = input()
  if s == ".":
    break
  answer.append(check(s))

for ans in answer:
  print(ans)
