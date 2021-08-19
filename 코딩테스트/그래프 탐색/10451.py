t = int(input())
answer = []
for _ in range(t):
  n = int(input())
  ans = 0
  lst = [0]+list(map(int,input().split()))
  visited = [False for _ in range(n+1)]
  for i in range(1,n+1):
    if not visited[i]:
      visited[i] = True
      ans += 1
      temp = lst[i]
      while True:
        if visited[temp]:
          break
        else:
          visited[temp] = True
          temp = lst[temp]
  answer.append(ans)

for ans in answer:
  print(ans)
