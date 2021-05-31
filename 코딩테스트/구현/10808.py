lst = [0 for _ in range(26)]
s = input()

for i in s:
  lst[ord(i)-97] += 1

for i in lst:
  print(i, end=" ")
