topl = 1
answer = 0
q = []

s = input()
for i in range(len(s)):
  if s[i] == "(":
    topl *= 2
    q.append(s[i])
  elif s[i] == '[':
    topl *= 3
    q.append(s[i])
  elif s[i] == ')' and q and q[-1] == '(':
    if s[i-1] == '(':
      answer += topl
    topl //= 2
    q.pop()
  elif s[i] == ']' and q and q[-1] =='[':
    if s[i-1] =='[':
      answer += topl
    topl //= 3
    q.pop()
  else:
    answer = 0
    break
if q:
  answer = 0

print(answer)
