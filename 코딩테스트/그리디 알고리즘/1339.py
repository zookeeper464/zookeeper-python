n = int(input())
dic = dict()
for _ in range(n):
  s = input()
  m = len(s)
  for idx, i in enumerate(s):
    try:
      dic[i] += 10**(m-idx-1)
    except:
      dic[i] = 10**(m-idx-1)

lst = list(dic.values())
lst.sort(reverse=True)
temp = 9
answer = 0
for i in lst:
  answer += temp*i
  temp -= 1

print(answer)
