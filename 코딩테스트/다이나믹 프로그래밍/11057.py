n = int(input())
lst = [1 for _ in range(10)]
for _ in range(n-1):
  for i in range(9):
    lst[i] = sum(lst[i:])

print(sum(lst)%10007)
