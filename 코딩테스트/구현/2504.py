s = input()
lst = [s[0]]
answer = 0
if s[0] == "(":
  temp = 2
elif s[0] == "[":
  temp = 3
else:
  temp = 0

for i in range(1,len(s)):
  if temp == 0:
    answer = 0
    break
  if s[i]=="(":
    temp *= 2
    lst.append(s[i])
  elif s[i]=="[":
    temp *= 3
    lst.append(s[i])
  elif lst and s[i]==")":
    x = lst.pop()
    if x == "(":
      if s[i-1] == "(":
        answer += temp
      temp //=2
    else:
      temp = 0
  elif lst and s[i]=="]":
    x = lst.pop()
    if x == "[":
      if s[i-1] == "[":
        answer += temp
      temp //=3
    else:
      temp = 0

print(answer)
