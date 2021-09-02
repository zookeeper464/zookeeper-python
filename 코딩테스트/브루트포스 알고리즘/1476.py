e,s,m = map(int,input().split())

for i in range(7980):
  if i%15+1 == e and i%28+1 == s and i%19+1 == m:
    break

print(i+1)
