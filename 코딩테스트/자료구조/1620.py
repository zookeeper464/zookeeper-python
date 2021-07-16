n,m = map(int,input().split())
num_lst, lst = dict(), [""]
for i in range(1,n+1):
  s = input()
  num_lst[s] = i
  lst.append(s)

answer = []
for _ in range(m):
  s = input()

  try:
    s = int(s)
    answer.append(lst[s])
  except:
    answer.append(num_lst[s])

for ans in answer:
  print(ans)
