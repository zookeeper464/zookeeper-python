n = int(input())
dic = dict()
for _ in range(n):
  s = input()
  l = len(s)
  for i in range(l):
    if s[i] not in dic.keys():
      dic[s[i]] = 10**(l-i-1)
    else:
      dic[s[i]] += 10**(l-i-1)

lst = list(dic.values())
lst.sort(reverse = True)

answer = 0
ls = len(lst)
for i in range(ls):
  answer += lst[i]*(9-i)

print(answer)
