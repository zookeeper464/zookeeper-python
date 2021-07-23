s = input()
answer = ''

for i in s:
  if ord(i)<65:
    answer += i
  elif ord(i)<97:
    answer += chr((ord(i)-65+13)%26+65)
  else:
    answer += chr((ord(i)-97+13)%26+97)

print(answer)
