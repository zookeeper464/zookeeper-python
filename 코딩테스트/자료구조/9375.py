t = int(input())
answer = []

for _ in range(t):
  n = int(input())
  dic = dict()
  for _ in range(n):
    s = input().split()
    try: dic[s[1]] += 1
    except: dic[s[1]] = 2
  cnt = 1
  for i in dic:
    cnt *= dic[i]
  cnt -= 1
  answer.append(cnt)
  
for ans in answer:
  print(ans)
