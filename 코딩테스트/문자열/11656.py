s = input()
n = len(s)
lst = []
for i in range(n):
  lst.append(s[i:])

lst.sort()
for i in lst:
  print(i)
