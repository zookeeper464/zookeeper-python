n = int(input())
lst = []
for _ in range(n):
  m = int(input())
  lst.append(m)
lst.sort(reverse = True)

m = 0
for i in range(n):
  m = max(lst[i]*(i+1),m)

print(m)
