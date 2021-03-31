s = list(input())

for i in range(len(s)):
  l = ord(s[i])
  if l >= 68:
    s[i] = chr((ord(s[i]) - 3))
  else:
    s[i] = chr((ord(s[i]) + 23))
  #abc와 나머지를 구분하여 연산한다.

print("".join(s))
