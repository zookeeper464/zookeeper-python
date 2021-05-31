s = input()


answer = 0
lst = [0 for _ in range(9)]
for i in s:
  if i =="9":
    lst[6] += 1
  else:
    lst[int(i)] += 1

lst[6] += 1
lst[6] //= 2

print(max(lst))
