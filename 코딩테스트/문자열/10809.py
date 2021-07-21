lst = [-1 for _ in range(26)]
s = input()
for idx, i in enumerate(s):
  n = ord(i)-97
  if lst[n] == -1:
    lst[n] = idx

for num in lst:
  print(num, end=' ')
