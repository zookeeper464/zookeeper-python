from collections import deque

dr,dc = [1,-1,0,0],[0,0,1,-1]

def bfs():
  if start == '123456780':
    return 0
    
  check = set([start])
  q = deque([(start, start.index("0"))])
  cnt = 0

  while q:
    cnt += 1
    for _ in range(len(q)):
      temp, idx = q.popleft()
      r, c = idx//3, idx%3

      for d in range(4):
        nr,nc = r+dr[d],c+dc[d]
        if not (0 <= nr < 3 and 0 <= nc < 3):
          continue

        lst = list(temp)
        n_idx = nr * 3 + nc
        lst[idx], lst[n_idx] = lst[n_idx], lst[idx]
        n_temp = ''.join(lst)
        
        if n_temp in check:
          continue

        elif '123456780' == n_temp:
          return cnt

        check.add(n_temp)
        q.append((n_temp, n_temp.index("0")))
        
  return -1

start = ""
for _ in range(3):
  start += ''.join(list(input().split()))

print(bfs())
