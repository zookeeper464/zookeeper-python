n = int(input())
dic = {}
answer = 0

for _ in range(n):
  s = input()
  l = len(s)
  for i in range(-l,0):
    try:
      dic[s[i]] += 10**(-1-i)
    except:
      dic[s[i]] = 10**(-1-i)
      
lst = sorted(list(dic.values()),reverse = True)

for i in range(len(lst)):
  answer += (9-i)*lst[i]

print(answer)
