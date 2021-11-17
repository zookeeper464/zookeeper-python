n,k = map(int,input().split())
lst = list(map(int,input().split()))
dic = {lst[i]:[] for i in range(k)}
answer = 0

for i in range(k-1,-1,-1):
  dic[lst[i]].append(i)

s = set()
for i in range(k):
  temp = dic[lst[i]].pop()
  if lst[i] in s:
    continue
  
  if len(s) < n:
    s.add(lst[i])
    continue
  
  temp = 0
  idx = 0
  for num in s:
    if dic[num] == []:
      temp = num
      break

    if idx<dic[num][-1]:
      idx = dic[num][-1]
      temp = num

  s -= {temp}
  s.add(lst[i])
  answer += 1

print(answer)
