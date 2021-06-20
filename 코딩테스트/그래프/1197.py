v, e = map(int,input().split())
dic = dict()
answer = 0
cnt = 0
s = False

for _ in  range(e):
  a,b,c = map(int,input().split())
  if c in dic:
    dic[c].append([a,b])
  else:
    dic[c] = [[a,b]]

e_visited = [[False for _ in range(v+1)] for _ in range(v+1)]
v_visited = [0 for _ in range(v+1)]
lst = list(dic.keys())
lst.sort()

for i in lst:
  for x, y in dic[i]:
    if cnt == v-1:
      s = True
      break
    if not e_visited[x][y] and v_visited[x]<2 and v_visited[y]<2:
      answer += i
      e_visited[x][y], e_visited[y][x] = True, True
      v_visited[x] += 1
      v_visited[y] += 1
      cnt += 1
  if s:
    break
print(answer)
