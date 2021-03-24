lst = list(input().upper())
s = list(set(lst))
answer = []
for i in s:
  answer.append(lst.count(i))

m = max(answer)
a = answer.count(m)
if a >1:
  print("?")
else:
  print(s[answer.index(m)])
