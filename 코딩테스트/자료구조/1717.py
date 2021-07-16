n,m = map(int,input().split())
lst = [-1 for _ in range(n+1)]
idx = []
answer =[]

for _ in range(m):
  c,a,b = map(int,input().split())
  if c == 0:
    if lst[a] == -1 and lst[b] == -1:
      lst[a] = len(idx)
      lst[b] = len(idx)
      idx.append(set([a,b]))
    else:
      # 두개 다 있으면 꺼내서 합치고 다시 넣는다.
      # 하나만 있으면 거기에 남은 하나를 넣는다.
      if lst[a] == -1:
        lst[a] = lst[b]
        idx[lst[a]].add(b)
      elif lst[b] == -1:
        lst[b] = lst[a]
        idx[lst[b]].add(b)
      elif lst[a] == lst[b]:
        pass
      else:
        temp_set, idx[lst[b]] = idx[lst[b]], set()
        for el in list(temp_set):
          lst[el] = lst[a]
        idx[lst[a]].update(list(temp_set))
    
  else:
    if lst[a] != -1 and lst[b] != -1 and lst[a] == lst[b]:
      answer.append('YES')
    elif a==b:
      answer.append('YES')
    else:
      answer.append('NO')

for ans in answer:
  print(ans)
