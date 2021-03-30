s = input()

for i in s:
  if ord(i) > 90:
    print(chr(ord(i)-32), end="")
  else:
    print(chr(ord(i)+32), end="")
