n = int(input())
lst = []
for _ in range(n):
  lst.append(int(input()))

dic = dict()
for i in lst:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1
m = max(dic.values())

answer = []
for i in dic:
  if dic[i] == m:
    answer.append(i)
answer.sort()

lst.sort()
print(round(sum(lst)/n))
print(lst[n//2])
if len(answer) == 1:
  print(answer[0])
else:
  print(answer[1])
print(max(lst)-min(lst))
