s = input()
n = len(s)
for i in range(n//10):
  for j in range(10):
    print(s[10*i+j], end="")
  print()
for i in range(10*(n//10),n):
  print(s[i], end="")
