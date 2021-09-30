n,m = map(int,input().split())
parent = list(range(n+1))
answer = []

def find(t):
  if t == parent[t]:
    return t
  
  parent[t] = find(parent[t])
  return parent[t]

def union (a,b):
  a,b = find(a), find(b)

  if a < b: parent[b] = a
  else: parent[a] = b

for _ in range(m):
  x,a,b = map(int,input().split())
  if x == 1:
    if find(a) == find(b):
      answer.append('YES')
    else:
      answer.append('NO')
  else:
    union(a,b)

print(*answer, sep='\n')
