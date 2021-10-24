n = int(input())
v_list = [[] for _ in range(n+1)]
topl = [0] * (n+1)
time_list = [0] * (n+1)
answer = [0] * (n+1)
t_list = [[] for _ in range(n+1)]

for i in range(1,n+1):
  lst = list(map(int,input().split()))
  time_list[i] = lst[0]
  topl[i] = len(lst)-2
  for j in range(1,len(lst)-1):
    v_list[lst[j]].append(i)
    t_list[i].append(lst[j])

while True:
  lst = []
  for i in range(1,n+1):
    if topl[i] == 0:
      topl[i] -= 1
      lst.append(i)
      if t_list[i]:
        answer[i] = time_list[i] + max([answer[k] for k in t_list[i]])
      else:
        answer[i] = time_list[i]

  for i in lst:
    for j in v_list[i]:
      topl[j] -= 1
  
  if not lst:
    break

for i in range(1,n+1):
  print(answer[i])
