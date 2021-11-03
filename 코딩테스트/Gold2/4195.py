def find (x):
  if x == parent[x]:
    return x
  else:
    p = find(parent[x])
    parent[x] = p
    return p

def union(x,y):
  x,y = find(x),find(y)
  
  if x != y:
    parent[y] = x
    number[x] += number[y]

def find_root (x):
  if x == parent[x]:
    return x
  else:
    p = find(parent[x])
    return p

t = int(input())
answer = []

for _ in range(t):
  f = int(input())
  parent = dict()
  number = dict()

  for _ in range(f):
    x,y = input().split()

    if x not in parent:
      parent[x] = x
      number[x] = 1

    if y not in parent:
      parent[y] = y
      number[y] = 1

    union(x,y)
    answer.append(number[find_root(y)])

print(*answer,sep='\n')
