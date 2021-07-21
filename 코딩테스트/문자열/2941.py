s= input()
n = len(s)
answer = n
for i in range(n-1):
  if s[i] == "c":
    n1 = s[i+1]
    if n1 == '-' or n1 =='=':
      answer -= 1
  
  elif s[i] == "l" or s[i] == "n":
    n1 = s[i+1]
    if n1 == 'j':
      answer -= 1
  
  elif s[i] == 's' or s[i] == 'z':
    n1 = s[i+1]
    if n1 == '=':
      answer -= 1

  elif s[i] == 'd':
    n1 = s[i+1]
    if n1 == '-':
      answer -= 1

    elif i < n-2:
      n2 = s[i+2]
      if n1+n2 == 'z=':
        answer -= 1

print(answer)
