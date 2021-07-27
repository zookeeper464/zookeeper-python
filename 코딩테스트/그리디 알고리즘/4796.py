answer = []
while True:
  l,p,v = map(int,input().split())
  if (l,p,v) == (0,0,0):
    break
    
  ans = l*(v//p) + min(l,v%p)
  answer.append(ans)

for idx, ans in enumerate(answer):
  print(f"Case {idx+1}: {ans}")
