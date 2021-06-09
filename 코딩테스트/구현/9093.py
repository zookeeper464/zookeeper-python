t = int(input())
lst = []
for _ in range(t):
  lst.append(input()[::-1])

for i in lst:
  print(i)
