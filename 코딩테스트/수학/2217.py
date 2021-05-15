n = int(input())
lst = []
for i in range(n):
  lst.append(int(input()))
lst.sort()
for i in range(len(lst)):
  lst[i] = lst[i]*(len(lst)-i)

print(max(lst))
