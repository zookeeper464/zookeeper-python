n,m = map(int,input().split())
q,parents = [],[i for i in range(n+1)]
answer = 0
for _ in range(m):
  a,b,c = map(int,input().split())
  q.append([c,a,b])
q.sort(key =lambda x: x[0])

def find(num):
  if parents[num]!=num:
    parents[num] = find(parents[num])
  
  return parents[num]

def union(a,b):
  a,b = find(a),find(b)
  parents[max(a,b)] = min(a,b)

for val,a,b in q:
  if find(a)!=find(b):
    union(a,b)
    answer += val
    last = val

print(answer-last)
