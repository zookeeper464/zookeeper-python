n = int(input())
lst = list(map(int, input().split()))
lst.sort()

num = 1
for i in range(n):
  if num < lst[i]:
    break
  num += lst[i]

print(num)
